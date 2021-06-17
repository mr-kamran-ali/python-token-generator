PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE tokens(
                                        id integer PRIMARY KEY,
                                        token text NOT NULL,
                                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                        UNIQUE(token)
                                    );
COMMIT;
