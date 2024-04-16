-- Create a table to store the language detection records
CREATE TABLE IF NOT EXISTS feedback (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    language VARCHAR(50) NOT NULL,
    correct BOOLEAN NOT NULL,

    CONSTRAINT unique_text_language UNIQUE (text, language)
);
