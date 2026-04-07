import requests
from utils import BASE_URL, get_headers

# ❌ Missing Header Bug
def test_missing_header():
    res = requests.post(f"{BASE_URL}/api/auth")
    assert res.status_code != 200


# ❌ Invalid Video ID
def test_invalid_video_id():
    res = requests.get(
        f"{BASE_URL}/api/videos/invalid123",
        headers=get_headers()
    )
    assert res.status_code in [400, 404]


# ❌ Duplicate Processing Bug
def test_duplicate_processing(auth_token):
    create = requests.post(
        f"{BASE_URL}/api/videos",
        headers=get_headers(auth_token),
        json={"title": "Duplicate Test"}
    )

    video_id = create.json()["id"]

    url = f"{BASE_URL}/api/videos/{video_id}/process-captions"

    r1 = requests.post(url, headers=get_headers(auth_token))
    r2 = requests.post(url, headers=get_headers(auth_token))

    # second call should ideally fail
    assert r2.status_code != 200


# ❌ Delete Before Processing Complete
def test_delete_before_processing(auth_token):
    create = requests.post(
        f"{BASE_URL}/api/videos",
        headers=get_headers(auth_token),
        json={"title": "Delete Early"}
    )

    video_id = create.json()["id"]

    delete_res = requests.delete(
        f"{BASE_URL}/api/videos/{video_id}",
        headers=get_headers(auth_token)
    )

    assert delete_res.status_code in [200, 204]