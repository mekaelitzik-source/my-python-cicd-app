# Python Flask CI/CD App

This is a simple Flask application used to practice CI/CD.

## Tools used

- GitHub Actions - used to automate testing, Docker build, and deployment
- Docker - used to package the app into a container image
- Docker Hub - used to store the Docker image
- Kubernetes - used to run the containerized app
- Terraform AWS - will be added later for infrastructure automation
- Argo CD - will be added later for GitOps deployment

## Endpoints

/ - Home page

/health - Health check endpoint used by Docker, Kubernetes, and CI/CD