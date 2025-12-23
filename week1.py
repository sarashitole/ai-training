import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        # Printing 3 fields from API response
        print("Type:", data["type"])
        print("Setup:", data["setup"])
        print("Punchline:", data["punchline"])

    except requests.exceptions.ConnectionError:
        print("❌ No internet connection.")

    except requests.exceptions.Timeout:
        print("❌ Request timed out.")

    except requests.exceptions.HTTPError:
        print("❌ API error.")

    except Exception as e:
        print("❌ Unexpected error:", e)


if __name__ == "__main__":
    get_joke()
