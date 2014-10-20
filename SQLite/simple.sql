-- Simple key-value database

CREATE TABLE Data (
  key TEXT PRIMARY KEY,
  value INTEGER
);

CREATE TABLE Results (
   experiment TEXT,
   result TEXT,
   value DOUBLE
 );
 