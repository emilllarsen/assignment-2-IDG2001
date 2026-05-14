"""API endpoint integration tests."""


class TestUsers:
    def test_create_user(self, client):
        response = client.post("/v2/user", json={
            "email": "test@example.com",
            "password": "secret123",
        })
        assert response.status_code == 201
        assert response.json()["email"] == "test@example.com"
        assert response.json()["tokens"] == 10

    def test_duplicate_user(self, client):
        client.post("/v2/user", json={
            "email": "dupe@test.com", "password": "secret123",
        })
        response = client.post("/v2/user", json={
            "email": "dupe@test.com", "password": "other456",
        })
        assert response.status_code == 409

    def test_get_user(self, client):
        create_response = client.post("/v2/user", json={
            "email": "find@test.com", "password": "secret123",
        })
        user_id = create_response.json()["id"]
        response = client.get(f"/v2/user/{user_id}")
        assert response.status_code == 200
        assert response.json()["email"] == "find@test.com"

    def test_delete_user(self, client):
        create_response = client.post("/v2/user", json={
            "email": "delete@test.com", "password": "secret123",
        })
        user_id = create_response.json()["id"]
        response = client.delete(f"/v2/user/{user_id}")
        assert response.status_code == 204


class TestTokens:
    # This test was for the assignment-1 version of POST /tokens which directly
    # added tokens via {user_id, amount}. In assignment 2 this endpoint changed
    # to the token-shop redemption flow and requires a live token-shop container.
    # def test_add_tokens(self, client):
    #     create_response = client.post("/v2/user", json={
    #         "email": "token@test.com", "password": "secret123",
    #     })
    #     user_id = create_response.json()["id"]
    #     response = client.post("/v2/tokens", json={
    #         "user_id": user_id, "amount": 5,
    #     })
    #     assert response.json()["tokens"] == 15

    def test_token_consumption(self, client):
        create_response = client.post("/v2/user", json={
            "email": "consume@test.com", "password": "secret123",
        })
        user_id = create_response.json()["id"]

        client.get("/v2/country/JAM", headers={"X-User-Id": user_id})

        response = client.get(f"/v2/user/{user_id}")
        assert response.json()["tokens"] == 9

    def test_no_tokens_returns_403(self, client):
        create_response = client.post("/v2/user", json={
            "email": "broke@test.com", "password": "secret123",
        })
        user_id = create_response.json()["id"]

        for _ in range(10):
            client.get("/v2/country/JAM", headers={"X-User-Id": user_id})

        response = client.get("/v2/country/JAM", headers={"X-User-Id": user_id})
        assert response.status_code == 403


class TestDataEndpoints:
    def test_get_athlete_returns_data(self, client):
        # All data endpoints need a user with tokens, so we make one first
        create_response = client.post("/v2/user", json={
            "email": "data@test.com",
            "password": "secret123",
        })
        user_id = create_response.json()["id"]

        # 2 Usain Bolt records are seeded in conftest.py
        response = client.get(
            "/v2/athlete/Usain-Bolt",
            headers={"X-User-Id": user_id},
        )

        assert response.status_code == 200
        assert response.json()["count"] == 2
        assert response.json()["results"][0]["noc"] == "JAM"

    def test_get_country_returns_data(self, client):
        # All data endpoints need a user with tokens, so we make one first
        create_response = client.post("/v2/user", json={
            "email": "country@test.com",
            "password": "secret123",
        })
        user_id = create_response.json()["id"]

        # A Norwegian skier is seeded in conftest.py
        response = client.get(
            "/v2/country/NOR",
            headers={"X-User-Id": user_id},
        )

        response_body = response.json()

        assert response.status_code == 200
        assert "Skiing" in response_body["sports"]

    def test_get_sport_returns_data(self, client):
        # All data endpoints need a user with tokens, so we make one first
        create_response = client.post("/v2/user", json={
            "email": "sport@test.com",
            "password": "secret123",
        })
        user_id = create_response.json()["id"]

        # 2 Athletics records are seeded in conftest.py
        response = client.get(
            "/v2/sport/Athletics",
            headers={"X-User-Id": user_id},
        )

        assert response.status_code == 200
        assert response.json()["count"] == 2

    def test_athlete_not_found_does_not_deduct_token(self, client):
        # Create a user with the default 10 tokens
        create_response = client.post("/v2/user", json={
            "email": "nodeduce@test.com",
            "password": "secret123",
        })
        user_id = create_response.json()["id"]

        # Search for an athlete that does not exist
        client.get(
            "/v2/athlete/nobody-ever",
            headers={"X-User-Id": user_id},
        )

        # Tokens should still be 10, we do not charge for failed requests
        user_response = client.get(f"/v2/user/{user_id}")
        token_count = user_response.json()["tokens"]

        assert token_count == 10
