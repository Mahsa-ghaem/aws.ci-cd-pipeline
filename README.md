 #### AWS CI/CD Pipeline — Serverless Demo

This project demonstrates a **complete CI/CD pipeline** that automatically tests, builds, and deploys a Python AWS Lambda function using **GitHub Actions**, **AWS SAM**, and **OpenID Connect (OIDC)** authentication — without using long-lived AWS keys.

--------------------------

### Overview

**Goal:**  
Deploy a simple Python Lambda that returns a JSON response through a public Function URL — automatically on every push to the `main` branch.

**Pipeline summary:**
1. GitHub Actions runs tests with `pytest`.
2. If tests pass, it builds the Lambda using **AWS SAM**.
3. SAM uploads build artifacts to an S3 bucket.
4. CloudFormation creates/updates the Lambda stack.
5. The Lambda Function URL becomes available immediately after deployment.

--------------------------

### Architecture

| Component | Purpose |
|------------|----------|
| **GitHub Actions** | CI/CD engine — runs tests, builds, and deploys via OIDC |
| **IAM Role (GitHubOIDC-Deploy-Dev)** | Lets GitHub Actions deploy securely to AWS |
| **AWS SAM / CloudFormation** | Infrastructure-as-Code definition (see `template.yaml`) |
| **S3 Bucket** | Stores build artifacts during deployment |
| **AWS Lambda** | Python function serving a JSON API endpoint |

--------------------------

### Repository Structure


- **app/** — Lambda function package (`app.py`, `__init__.py`)
- **tests/** — pytest unit tests
- **template.yaml** — AWS SAM template
- **requirements.txt** — Python test dependencies
- **.github/workflows/** — CI/CD workflow (`cicd.yml`)


--------------------------

### Deployment Flow

1. We push the code to the `main` branch.  
2. GitHub Actions automatically:
   - Runs `pytest`  
   - Builds the Lambda with SAM  
   - Deploys via CloudFormation  
3. AWS Lambda and Function URL are created/updated.  
4. Open the Function URL in a browser to view JSON output.

--------------------------

### Example Lambda Response

```json
{
  "message": "CI/CD on AWS via GitHub Actions + OIDC + SAM — success",
  "path": "/"
}
```

--------------------------

### Prerequisites

- AWS account (with OIDC role configured)

- GitHub repository

- Python 3.12

- AWS SAM CLI installed

--------------------------


### How to Run Locally

```bash
pip install -r requirements.txt
pytest -q
```

-------------------------

## Author

Created by Mahsa Ghaempanah — educational DevOps / Serverless demo project.















