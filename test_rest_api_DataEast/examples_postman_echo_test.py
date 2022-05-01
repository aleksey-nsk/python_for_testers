# -*- coding: utf-8 -*-

import requests


def test_get_example():
    print("\n\n************** Test get example **************")

    # Arrange
    url = "https://postman-echo.com/get"
    params = {
        "foo1": "bar1",
        "foo2": "bar2"
    }

    # Act
    response = requests.get(url=url, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("url") == "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
    assert response_json.get("args").get("foo1") == "bar1"
    assert response_json.get("args").get("foo2") == "bar2"
    assert response_json.get("args") == params


def test_post_example():
    print("\n\n************** Test post example *************")

    # Arrange
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {
        "title": "First POST request",
        "body": "I hope, it’s gonna be work",
        "userId": 12345
    }
    headers = {
        "Content-Type": "application/json"
    }
    response_expected_body = {
        "title": "First POST request",
        "body": "I hope, it’s gonna be work",
        "userId": 12345,
        "id": 101
    }

    # Act
    response = requests.post(url=url, json=body, headers=headers)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 201
    assert response_json.get("title") == "First POST request"
    assert response_json.get("body") == "I hope, it’s gonna be work"
    assert response_json.get("userId") == 12345
    assert response_json.get("id") == 101
    assert response_json == response_expected_body
