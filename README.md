 #### AWS CI/CD Pipeline — Python Lambda(Manual Infrastructure)

This project demonstrates a **continuous integration and delivery (CI/CD)** pipeline that automatically tests and deploys a Python AWS Lambda function using **GitHub Actions** and **OpenID Connect (OIDC)**. 

--------------------------

### Overview

**Goal:**  
Deploy a simple Python Lambda that returns a JSON response through a public Function URL — automatically on every push to the `main` branch.

**Concept:**  
All AWS resources (Lambda, S3, IAM role) are created manually once in the AWS Console.
After that, GitHub Actions automatically handles **testing and deployment** whenever code changes are pushed.

------------------------------

**Workflow Summary**
1. GitHub Actions runs tests with `pytest`.
2. If tests pass, it zips the Lambda source code.
3. Using the configured OIDC IAM role, GitHub updates the Lambda function code automatically. 
4. The new version is instantly live through the Lambda Function URL.

--------------------------

### Repository Structure

| Path | Description |
|------------|----------|
| `app/` | Python Lambda code (`app.py`, `__init__.py`) |
| `tests/` | Unit tests executed by `pytest`|
| `requirements.txt` | Test dependencies |
| `.github/workflows/cicd.yml` | CI/CD workflow — installs Python, runs tests, zips the code, and deploys to AWS Lambda |

--------------------------

### AWS Setup


- **S3 bucket** — created manually for optional data storage.
  Example : `portfolio-cicd-dev-mahsa-eu-central-1`.
- **tests/** — pytest unit tests
- **Lambda function** — created manually with:
  - Name : `portfolio-cicd-dev-function-mahsa`
  - Runtime: Python 3.12
  - Handler: `app.lambda_handler`
  - Function URL enabled (auth type: NONE) ? gives an HTTPS endpoint.

- **IAM Role** (`GitHubOIDC-Deploy-Dev`) — allows GitHub Actions to deploy code via OIDC, using only short-lived credentials. Key permissions: 
  - `lambda:PublishVersion`
  - `lambda:UpdateFunctionCode`

--------------------------

### How the CI/CD Works

Each time code is pushed to `main`:

1. GitHub Actions starts a new virtual environment.  
2. It installs Python and dependencies from `requirements.txt`.
3. It runs the tests using `pytest`.  
4. If successful, it updates the Lambda function code through AWS API calls.

This ensures automated testing and deployment without running any AWS CLI or SAM commands manually.

--------------------------

### Example Lambda Response

```json
{
  "message": "CI/CD on AWS via GitHub Actions + OIDC — success",
  "path": "/"
}
```

--------------------------


### How to Test Locally

```bash
pip install -r requirements.txt
pytest -q
```

-------------------------

## Author

Created by Mahsa Ghaempanah — educational DevOps / Serverless demo project using manual AWS setup and automated CI/CD.















