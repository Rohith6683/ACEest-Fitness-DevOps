# ACEest Fitness & Gym - DevOps Assignment

## Overview
A Flask-based fitness and gym management application demonstrating
version control, automated testing, continuous integration,
containerization, static code analysis and Kubernetes deployment
strategies.

## Technology Stack
- Python 3.9
- Flask
- Pytest and Pytest-Cov
- Git and GitHub
- Docker
- Jenkins
- GitHub Actions
- SonarQube
- Kubernetes
- Minikube

## Application Versions
- v1.0: Core fitness and membership management APIs.
- v1.1: Membership plans API and additional automated test.

## Project Structure
- app.py: Flask application
- tests/test_app.py: Automated tests
- requirements.txt: Python dependencies
- Dockerfile: Docker build configuration
- Jenkinsfile: Jenkins CI pipeline
- .github/workflows/main.yml: GitHub Actions workflow
- k8s/deployment.yaml: Kubernetes deployment
- k8s/service.yaml: Kubernetes service
- k8s/blue-green.yaml: Blue-Green deployment
- k8s/canary.yaml: Canary deployment

## Local Setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python app.py

## Automated Testing

    python -m pytest -v

Generate coverage report:

    python -m pytest -v --cov=app --cov-report=term-missing --cov-report=xml:coverage.xml

Results:
- 7 automated tests passed.
- 89.7% line coverage.

## Docker

    docker build -t aceest-fitness:1.1 .
    docker run --rm -p 5000:5000 aceest-fitness:1.1

Health verification:

    curl http://localhost:5000/health

## Jenkins CI Pipeline
The Jenkins pipeline includes:
1. Source code checkout.
2. Docker image build.
3. Automated Pytest execution inside Docker.
4. Docker image archival and fingerprinting.
5. Automated SCM polling.

## GitHub Actions
The workflow executes on pushes and pull requests.
It installs dependencies, runs automated tests and builds
the Docker image.

## SonarQube Analysis
Observed analysis results:
- Quality Gate: Passed
- Bugs: 0
- Vulnerabilities: 0
- Code Smells: 0
- Security Hotspots Reviewed: 100%
- Code Coverage: 89.7%
- Code Duplication: 0%
- Reliability Rating: A
- Security Rating: A
- Maintainability Rating: A
- Security Review Rating: A

## Kubernetes Setup

    minikube start --driver=docker --cpus=2 --memory=3072
    minikube image load aceest-fitness:1.0
    minikube image load aceest-fitness:1.1

## Rolling Deployment

    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml

Application service port: 30080

Demonstrated:
- Initial deployment of version 1.0.
- Rolling update to version 1.1.
- Successful rollback to version 1.0.
- Healthy application responses after transitions.

## Blue-Green Deployment

    kubectl apply -f k8s/blue-green.yaml

Application service port: 30081

Demonstrated:
- Blue environment running version 1.0.
- Green environment running version 1.1.
- Successful traffic switching to Green.
- Successful rollback to Blue.

## Canary Deployment

    kubectl apply -f k8s/canary.yaml

Application service port: 30082

Initial deployment:
- 4 stable replicas running version 1.0.
- 1 canary replica running version 1.1.

Observed traffic distribution:
- Stable: 82 requests out of 100.
- Canary: 18 requests out of 100.
- Failed requests: 0.

Canary promotion:
- 100 out of 100 requests served by version 1.1.
- Failed requests: 0.

Canary rollback:
- 100 out of 100 requests served by version 1.0.
- Failed requests: 0.

## Limitations
The application uses in-memory storage for demonstration purposes.
Traffic distribution is approximate and depends on Kubernetes
service load balancing. Post-deployment health checks do not
independently establish continuous zero downtime.

## Repository
https://github.com/Rohith6683/ACEest-Fitness-DevOps

## Shadow Deployment

Shadow deployment is implemented using an NGINX reverse
proxy with Kubernetes services and traffic mirroring.

- Production environment: ACEest Fitness v1.0
- Shadow candidate environment: ACEest Fitness v1.1
- NGINX image: nginx:1.28-alpine
- Configuration: k8s/shadow.yaml
- NodePort: 30083

### Deployment Commands

    kubectl apply -f k8s/shadow.yaml
    kubectl rollout status deployment/aceest-shadow-proxy
    curl http://$(minikube ip):30083/health

### Traffic Mirroring Results

| Metric | Result |
|---|---:|
| Total client requests | 100 |
| Production backend requests | 100 |
| Shadow candidate backend requests | 100 |
| Production responses to clients | 100 |
| Candidate responses to clients | 0 |
| Failed requests | 0 |
| NGINX errors reported | 0 |
| Health check | Healthy |

The shadow candidate received mirrored traffic without
affecting the production responses during the test.

