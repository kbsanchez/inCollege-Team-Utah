CREATE TABLE IF NOT EXISTS Username(
    username TEXT PRIMARY KEY,
    password TEXT,
    firstname TEXT,
    lastname TEXT,
    logedIn NOT NULL CHECK (logedIn IN (0, 1)) DEFAULT 0,
    email BOOLEAN NOT NULL CHECK (email IN (0, 1)) DEFAULT 1,
    sms BOOLEAN NOT NULL CHECK (sms IN (0, 1)) DEFAULT 1,
    marketing BOOLEAN NOT NULL CHECK (marketing IN (0, 1)) DEFAULT 1,
    language TEXT DEFAULT 'english'
);

CREATE TABLE IF NOT EXISTS Profile(
    username TEXT PRIMARY KEY,
    title TEXT, 
    major TEXT,
    universityName,
    about
);

CREATE TABLE IF NOT EXISTS Experience(username TEXT, title TEXT, employer TEXT, startDate TEXT, endDate TEXT, location TEXT, description TEXT);

CREATE TABLE IF NOT EXISTS Education(username TEXT, schoolName TEXT, degree TEXT, yearsAttended INTEGER);