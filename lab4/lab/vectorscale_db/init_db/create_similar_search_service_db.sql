-- prepare_similar_search_service_db.sql

-- create the database for similar search service
-- CREATE DATABASE similarity_search_service_db;

-- connect to the database
\c similarity_search_service_db

--- enable vector scale extension
CREATE EXTENSION IF NOT EXISTS vector CASCADE;