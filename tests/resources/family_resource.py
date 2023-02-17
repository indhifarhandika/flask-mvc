def test_family_resource(client):
    # Test List All
    response = client.get("/api/v1/family")
    assert response.status_code == 200

    TOTAL = response.json["data"]["total"]

    # Test Create New
    FIRST_NAME = "Test"
    response = client.post(
        "/api/v1/family",
        json={
            "name": FIRST_NAME,
            "chief_person_id": 2,
        },
    )
    assert response.status_code == 200
    ID = response.json["data"]["id"]

    response = client.get("/api/v1/family")
    assert response.status_code == 200

    new_total = response.json["data"]["total"]
    assert TOTAL + 1 == new_total

    # Test Get 1
    response = client.get(f"/api/v1/family?id={ID}")
    assert response.status_code == 200

    # Test Update
    SECOND_NAME = "Test 2"
    response = client.put(
        "/api/v1/family",
        json={
            "id": ID,
            "name": SECOND_NAME,
        },
    )
    assert response.status_code == 200

    name = response.json["data"]["name"]
    assert name == SECOND_NAME

    # Test Delete
    response = client.delete(f"/api/v1/family?id={ID}")
    assert response.status_code == 200

    response = client.get("/api/v1/family")
    assert response.status_code == 200

    new_total = response.json["data"]["total"]
    assert TOTAL == new_total
