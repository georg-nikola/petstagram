#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER petstagram;
	CREATE DATABASE petstagram;
	GRANT ALL PRIVILEGES ON DATABASE petstagram TO petstagram;
EOSQL