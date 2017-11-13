import sqlite3
import glob

from flask import Flask, request, jsonify, send_file
app = Flask(__name__)

def cacheFromRow(row):
    """Takes a db row from the geocache table and converts it into a
    JSON-compatible dictionary."""
    return {
        "id": row[0],
        "title": row[1],
        "details": row[2],
        "creator": row[3],
        "reward": row[4],
        "latitude": row[5],
        "longitude": row[6]
    } 

@app.route('/')
def welcome():
    return 'Welcome to the server backend for CS11 Swift GeoCache App'

@app.route('/createCache', methods=['POST'])
def createCache():
    """Create a new cache based on the information in the request.
    Put it in the database.
    This takes a JSON object in the request data with the following info:
    id - the unique id of the geocache
    title - the title of the geocache
    details - some extra information about the geocache
    creator - the creator of the geocache
    reward - what you get at the location
    latitude - the latitude, obviously
    longitude - duh.

    It's ok for latitude and longitude to be missing from the dictionary.
    If the id field is non-unique, returns the JSON object
    ["Failure"], otherwise returns ["Success"]
    """
    info = request.get_json()
    newId = info["id"]
    title = info["title"]
    details = info["details"]
    creator = info["creator"]
    reward = info["reward"]
    latitude = None
    longitude = None
    if "latitude" in info:
        latitude = info["latitude"]
    if "longitude" in info:
        longitude = info["longitude"]

    conn = sqlite3.connect('cache.db')
    c = conn.cursor()
    try:
        if latitude and longitude:
            c.execute('INSERT INTO geocache(id, title, details, creator, reward, latitude, longitude) VALUES (?,?,?,?,?,?,?)', (newId, title, details, creator, reward, latitude, longitude))
        else:
            c.execute('INSERT INTO geocache(id, title, details, creator, reward) VALUES (?,?,?,?,?)', (newId, title, details, creator, reward))

        conn.commit()
        result = "Success"
    except sqlite3.IntegrityError:
        result = "Failure"
        
    conn.close()

    return jsonify([result])

@app.route('/addPicture', methods=['POST'])
def addPicture():
    """
    Add a new picture to the cache with ID given in the request.
    Accessed with URL agument `id`, with the request body being the .png
    data of the image. Honor-system, don't send this anything bad :P
    """
    d = request.get_data()
    cacheID = request.args.get('id', '')
    filename = str(cacheID)
    number = len(glob.glob('Images/' + str(cacheID) + '*'))
    filename += '_' + str(number) + '.jpg'
    open('Images/' + filename, 'wb').write(d)
    return "Thanks for the picture!"

@app.route('/markComplete', methods=['POST'])
def markComplete():
    """Mark a completion in the database. Takes JSON with these fields:
    cacheid - the geocache id
    name - the name of the person completing the geocache.
    """
    info = request.get_json()
    cacheid = info["cacheid"]
    name = info["name"]

    conn = sqlite3.connect('cache.db')
    c = conn.cursor()
    c.execute('INSERT INTO completion(id, name) VALUES (?,?)', (cacheid, name))
    conn.commit()
    conn.close()

    return "Congrats on completing the cache!"

@app.route('/getDetails', methods=['GET'])
def getDetails():
    """Get the details of the cache with the given id.
    Since this is simple, just use the url
    /getDetails?id=<>
    Returns a json object with the details:
    title
    details
    creator
    reward
    latitude
    longitude
    """
    cacheid = request.args.get('id', '')

    conn = sqlite3.connect('cache.db')
    c = conn.cursor()
    c.execute('SELECT * FROM geocache WHERE id = ?', cacheid)
    row = c.fetchone()
    return jsonify(cacheFromRow(row))

@app.route('/getImageCount', methods=['GET'])
def getImageCount():
    """Get the number of images stored for a given geocache.
    Use the url
    /getImageCount?id=<>
    Returns a simple number.
    """
    cacheid = request.args.get('id', '')

    return jsonify(len(glob.glob('Images/' + str(cacheid) + '*')))

@app.route('/getImage', methods=['GET'])
def getImage():
    """Get the given image.
    Use the url
    /getImage?id=<>&img=<>
    """
    cacheid = request.args.get('id', '')
    img = request.args.get('img', '')
    return send_file('Images/' + str(cacheid) + '_' + str(img) + '.jpg')

@app.route('/getCaches', methods=['GET'])
def getCaches():
    """Get some info on all caches in the database.
    Returns a JSON object with an array of these:
    {
        id
        title
        details
        creator
        reward
        latitude
        longitude
    }
    """
    conn = sqlite3.connect('cache.db')
    c = conn.cursor()
    caches = c.execute('SELECT * FROM geocache')

    results = [cacheFromRow(row) for row in caches]
    return jsonify(results)

