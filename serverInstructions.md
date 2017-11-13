# CS 11 Swift/iOS
## Lab 5 Server Directions

To test out your app's network request features, you'll need a server to run
them against - the easiest way to do this is by hosting it locally. This is
not too hard - all you need are these two files:

[cacheServer.py](cacheServer.py)  
[makeGeoCache.sql](makeGeoCache.sql)

Put those in a directory to use for this server.

You will need to have Python installed, as well as sqlite3 (which comes with
most Python installations). You will also need the Flask package in Python,
you can install it with pip (`pip install flask`) or look at directions
[here](http://flask.pocoo.org).

Once you have these things, you're ready to start. First, you need to create
the sqlite database that the server expects. This is done by the
makeGeoCache.sql file. Sqlite databases are stored on your computer as single
files, and invoking `sqlite3 <filename>` will start sqlite on the given
database file, creating it if it doesn't exist. So, run

`
$ sqlite3 cache.db < makeGeoCache.sql
`

and you'll create the empty GeoCache database in the file `cache.db`.
With this created, the server is ready to run - in your server folder where
you put both files (the `cache.db` file should be there now too) just run

`
$ export FLASK_APP=cacheServer.py  
$ python -m flask run
`

Flask will tell you it's serving the app at `http://127.0.0.1:500/` (aka
`localhost:5000`) - if you go there in a web browser you should see a little
message that you're at the server backend for the GeoCache app, and you're
ready to make some requests to it from the app!
