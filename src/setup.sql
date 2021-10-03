CREATE TABLE IF NOT EXISTS user(
    username TEXT PRIMARY KEY,
    password TEXT,
    firstname TEXT,
    lastname TEXT,
    loggedIn NOT NULL CHECK (loggedIn IN (0, 1)) DEFAULT 0,
    email BOOLEAN NOT NULL CHECK (email IN (0, 1)) DEFAULT 1,
    sms BOOLEAN NOT NULL CHECK (sms IN (0, 1)) DEFAULT 1,
    marketing BOOLEAN NOT NULL CHECK (marketing IN (0, 1)) DEFAULT 1,
    language TEXT DEFAULT 'english'
);