import requests

def get_diff(diff_url):
    headers = {
        # tell GitHub need diff format
        "Accept": "application/vnd.github.v3.diff"
    }

    response = requests.get(diff_url, headers=headers)

    # Prevent error
    if response.status_code != 200:
        print("Failed to fetch diff:", response.status_code)
        return None

    return response.text
