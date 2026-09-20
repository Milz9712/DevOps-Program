import requests

try:
    response = requests.get(
        "https://api.github.com",
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    print(f"API request successful: {response.status_code}")
    print(f"Current user API: {data['current_user_url']}")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as error:
    print(f"API request failed: {error}")
