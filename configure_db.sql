CREATE DATABASE ibanapp;
CREATE USER ibanappuser WITH PASSWORD 'ibanapppasswd';
ALTER ROLE ibanappuser SET client_encoding TO 'utf8';
ALTER ROLE ibanappuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE ibanappuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ibanapp TO ibanappuser;
ALTER USER ibanappuser CREATEDB;