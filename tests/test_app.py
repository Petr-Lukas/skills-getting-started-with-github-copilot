def test_get_activities(client):
    r = client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_prevent_duplicate(client):
    email = "tester@mergington.edu"
    activity = "Chess Club"

    # first signup should succeed
    r1 = client.post(f"/activities/{activity}/signup?email={email}")
    assert r1.status_code == 200

    # duplicate signup should be rejected
    r2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert r2.status_code == 400


def test_remove_participant(client):
    email = "remove-me@mergington.edu"
    activity = "Programming Class"

    # ensure participant exists
    r1 = client.post(f"/activities/{activity}/signup?email={email}")
    assert r1.status_code == 200

    # remove participant
    r2 = client.delete(f"/activities/{activity}/participants?email={email}")
    assert r2.status_code == 200
    data = r2.json()
    assert "participants" in data
    assert email not in data["participants"]
