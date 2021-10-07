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
    username TEXT,
    title TEXT, 
    major TEXT,
    universityName,
    about,
    experiencesID INTEGER,
    educationID INTEGER
);