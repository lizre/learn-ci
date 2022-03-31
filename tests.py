
"""
This script contains tests that the app included the word "app", and that the http request
returns 200 status.
 Code is from https://circleci.com/blog/setting-up-continuous-integration-with-github/

"""

from app import app
with app.test_client() as test_client:
    response = test_client.get('/')
    assert b"app" in response.data, "app didn't say it was an app!"
    assert response.status_code == 200, "http request failed"

