import requests
import time
import json

def check_api(url):
    try:
        start_time = time.perf_counter()

        response = requests.get(url, timeout=5)

        end_time = time.perf_counter()

        response.raise_for_status()

        response_time = (end_time - start_time) * 1000

        if response_time >= 500:
            status = "slow"
        else:
            status = "healthy"

        return {
            "status": status,
            "status_code": response.status_code,
            "response_time": response_time
        }

    except requests.exceptions.RequestException:
        return {
            "status": "unhealthy",
            "status_code": None,
            "response_time": None
        }


apis = [
    {
        "name": "GitHub",
        "url": "https://api.github.com"
    },
    {
        "name": "Python",
        "url": "https://www.python.org"
    }
]

all_healthy = True

results = []

for api in apis:
    result = check_api(api["url"])

    results.append({
    "name": api["name"],
    "url": api["url"],
    "status": result["status"],
    "status_code": result["status_code"],
    "response_time": result["response_time"]
})

    results.append(result)

    if result["status"] != "healthy":
        all_healthy = False

    if result["response_time"] is not None:
        print(
            f"{api['name']}: "
            f"{result['status']} "
            f"({result['status_code']}) - "
            f"{result['response_time']:.2f} ms"
        )
    else:
        print(
            f"{api['name']}: "
            f"{result['status']}"
        )

with open("api_health_report.json", "w") as file:
    json.dump(results, file, indent=4)

print("API report saved to api_health_report.json")

if all_healthy:
    print("Overall API status: HEALTHY")
else:
    print("Overall API status: WARNING")