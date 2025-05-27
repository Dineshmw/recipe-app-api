# Recipe API Project

A RESTful API built with **Django** and **Django REST Framework**, as taught in the Udemy course _"Build a Backend REST API with Python & Django - Advanced"_.

This project provides a backend for managing recipes, ingredients, and tags. It also includes user authentication using token-based auth.

## Features

- User registration and authentication
- Create, update, and delete recipes
- Upload and associate images with recipes
- Assign tags and ingredients to recipes
- Filter recipes by tags or ingredients
- Fully tested with unit and integration tests
- Dockerized for easy development and deployment

## Tech Stack

- Python 3.11+
- Django 4+
- Django REST Framework
- Postgres (via Docker)
- Gunicorn (for production)
- flake8 (for linting)
- drf-spectacular (for OpenAPI schema generation)

---

## Getting Started

These instructions will help you set up the project on your local machine.

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Make (optional, for using Makefile shortcuts)

### Clone the Repository

```bash
git clone https://github.com/yourusername/recipe-api.git
cd recipe-api
```

### Build and Run with Docker

```bash
docker-compose build
docker-compose up
```

Or using Make:

```bash
make build
make up
```

The API will be available at: `http://localhost:8000/api/`

Admin panel: `http://localhost:8000/admin/`

---

## Running Tests

To run tests:

```bash
docker-compose run --rm app sh -c "python manage.py test"
```

Or using Make:

```bash
make test
```

---

## Linting

To check code quality with flake8:

```bash
docker-compose run --rm app sh -c "flake8"
```

Or:

```bash
make lint
```

---

## API Documentation

Once the server is running, access auto-generated API documentation:

- Swagger UI: `http://localhost:8000/api/docs/swagger/`
- Redoc: `http://localhost:8000/api/docs/redoc/`

---

## Project Structure

```
.
├── app/                # Django app source
├── .github/            # GitHub Actions CI workflows
├── docker-compose.yml  # Docker services configuration
├── Dockerfile          # Docker image definition
├── manage.py           # Django CLI entry point
├── requirements.txt    # Python dependencies
└── README.md
```

---

## License

MIT License - see the [LICENSE](LICENSE) file for details.

---

## Credits

Based on the [Udemy course](https://www.udemy.com/course/django-python-advanced/) by Mark Winterbottom.
