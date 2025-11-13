import app.app as app

def test_lambda_handler_returns_json_ok():
    event = {"rawPath": "/test"}
    res = app.lambda_handler(event, None)
    assert isinstance(res, dict)
    assert res.get("statusCode") == 200    # HTTP protocol
    assert "v2" in res.get("body", "")     # it checks if the word "v2" exits inside the Lambda's response body.
