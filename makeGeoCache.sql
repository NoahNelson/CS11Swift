/* Clean up old tables. */

DROP TABLE IF EXISTS geocache;
DROP TABLE IF EXISTS completion;

/* Table of geocaches. */
CREATE TABLE geocache (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(30) NOT NULL,
  details VARCHAR(1000) NOT NULL,
  creator VARCHAR(100) NOT NULL,
  reward VARCHAR(100) NOT NULL,
  latitude NUMERIC(10, 7),
  longitude NUMERIC(10, 7)
);

/* Table describing who has completed which geocaches. */
CREATE TABLE completion (
  id INTEGER,
  name VARCHAR(100),
  PRIMARY KEY (id, name)
);
