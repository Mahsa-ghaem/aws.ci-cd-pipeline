import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": "CI/CD on AWS via GitHub Actions + OIDC - success",
            "path": (event or {}).get("rawPath", "/")

        })
    }
