import requests
import time
from utils import BASE_URL, get_headers

def test_full_flow(auth_token):

    # 1. Create video
    create_res = requests.post(
        f"{BASE_URL}/api/videos",
        headers=get_headers(auth_token),
        json={"title": "Test Video"}
    )

    assert create_res.status_code in [200, 201, 202]

    data = create_res.json()
    assert "id" in data
    video_id = data["id"]

    # 2. Trigger caption processing
    trigger_res = requests.post(
        f"{BASE_URL}/api/videos/{video_id}/process-captions",
        headers=get_headers(auth_token)
    )

    assert trigger_res.status_code in [200, 201, 202]

    # 3. Poll for captions (async handling)
    captions = None

    for _ in range(6):
        time.sleep(2)

        cap_res = requests.get(
            f"{BASE_URL}/api/captions",
            headers=get_headers(auth_token),
            params={"videoId": video_id}
        )

        if cap_res.status_code == 200 and cap_res.json():
            captions = cap_res.json()
            break

    assert captions is not None, "Captions not generated"

    # 4. Cleanup
    delete_res = requests.delete(
        f"{BASE_URL}/api/videos/{video_id}",
        headers=get_headers(auth_token)
    )

    assert delete_res.status_code in [200, 204]