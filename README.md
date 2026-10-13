# ACEest Fitness & Gym — DevOps Assignment

## Overview
ACEest Fitness & Gym is a Flask-based application used to demonstrate
Git version control, automated testing, Docker containerization, and CI
using Jenkins and GitHub Actions.

## Technology Stack
- Python 3.9
- Flask
- Pytest
- Git and GitHub
- Docker
- Jenkins
- GitHub Actions

## Project Structure
- app.py: Flask application and API endpoints
- tests/test_app.py: automated application tests
- requirements.txt: Python dependencies
- Dockerfile: Docker image build instructions
- .dockerignore: files excluded from Docker build context
- .gitignore: files excluded from Git tracking
- .github/workflows/main.yml: GitHub Actions workflow

## Local Setup
Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Run Tests
Execute the automated tests:

    python -m pytest -v

## Run the Application
Start Flask:

    python app.py

The application listens on port 5000. Check the health endpoint at:

    http://localhost:5000/health

## Docker
Build the image:

    docker build -t aceest-fitness:1.0 .

Run the container:

    docker run --rm -p 5000:5000 aceest-fitness:1.0

Check the health endpoint:

    curl http://localhost:5000/health

## Jenkins
The ACEest-Fitness-CI Jenkins pipeline:
1. Checks out the latest code from the main branch.
2. Installs Python dependencies.
3. Runs Pytest.
4. Builds the Docker image.
5. Starts a temporary container and verifies the health endpoint.
6. Removes the temporary test container.

## GitHub Actions
The workflow in .github/workflows/main.yml runs on pushes and pull
requests. It installs dependencies, executes automated tests, and builds
the Docker image.

## Repository
https://github.com/Rohith6683/ACEest-Fitness-DevOps
