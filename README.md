
# Petstagram

Petstagram is a fun and interactive platform where users can share pictures of their pets, just like Instagram.

## Description

This project is built using Django, a high-level Python Web framework. It uses PostgreSQL as its database and Gunicorn as its HTTP server. The project also uses the Pillow library for image processing.


## Docker Setup

This project uses Docker for easy setup and deployment. Here's how to get started:

1. Install Docker and Docker Compose on your machine. You can find the instructions on the official Docker docs.

2. Build the Docker images:

```bash
docker-compose build

docker-compose up

docker-compose down
```

## Local Setup (Without Docker)

If you prefer not to use Docker, you can set up the project locally. Here's how to get started:

1. Install Python and pip on your machine. You can find the instructions on the official Python docs.

2. Install PostgreSQL on your machine. You can find the instructions on the official PostgreSQL docs.

3. Create a database in PostgreSQL:

```bash
psql -U postgres -c "CREATE DATABASE petstagram_db;"
```

## Installation

This project uses pip for package management. Install the project dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

To run the project, use the following command:

```bash
python manage.py runserver
```

## Features

- Users can post pictures of their pets.
- Users can like and comment on posts.
- Users can follow other users and see their posts in a feed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


