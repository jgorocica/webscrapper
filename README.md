# WebScraper
Web Scrapping tool for Koombea

Tools: 
- Docker
- Docker Compose
- Scrapy
- Django
- PostgreSQL


This ReadMe file provides a step-by-step guide on how to set up a Django project using Docker and Docker Compose. This setup allows for easy deployment and development of your Django application.

Prerequisites

Before starting, make sure you have the following installed on your machine:

- Docker: Install Docker
- Docker Compose: Install Docker Compose


## Getting Started

To get started, please follow the next steps:

Clone the repository:

``
git clone <repository-url>
``

Replace <repository-url> with the URL of your Django project repository.

Navigate to the project directory:

``
cd <project-directory>
``
Replace `<project-directory>` with the name of your Django project directory.

Build the Docker images and start the containers:
``
docker-compose up --build
``

Access the Django application:

Open your web browser and go to http://localhost:8000


## Ensure you setup the envvars properly 
There is a file named `template.env`, copy and paste as `.env`

Set the database user and password, as corresponds. 

## Questions?
Feel free to reach me: eduar881@gmail.com

