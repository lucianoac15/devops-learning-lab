Simple FastAPI project used to learn DevOps and CI/CD.

## Development

- **Tests:** `pytest` (run from project root after `pip install -r requirements.txt`).
- **CI/CD:** GitHub Actions run tests and build the Docker image on pull requests and pushes to `main`.
- **Docker:** The project includes a `Dockerfile` to package the API; build with `docker build -t text-analysis-api .`.
