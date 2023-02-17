def test_get_all(client):
    response = client.get("/api/v1/family")
    assert response.status_code == 200


def test_others(client):
    response = client.post(
        "/api/v1/family",
        json={
            "name": "Test",
            "chief_person_id": 2,
        },
    )
    print(response.data)
    assert response.status_code == 200
