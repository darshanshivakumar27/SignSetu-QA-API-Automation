BASE_URL = "https://qa-testing-navy.vercel.app"

HEADERS = {
    "X-Candidate-ID": "Darshan_S"
}

def get_headers(token=None):
    headers = HEADERS.copy()

    # Add token only if available
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"

    return headers