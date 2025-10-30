import app.app as app

def test_lambda_handler_returns_json_ok():
    event = {"rawPath": "/test"}
    res = app.lambda_handler(event, None)
    assert isinstance(res, dict)
    assert res.get("statusCode") == 200
    assert "success" in res.get("body", "")
