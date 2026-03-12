import requests

url = "http://paceitplaylists.geoclaster.xyz/m3u.php"
headers = {
    "User-Agent": "okhttp/4.12.0",
}

def fetch_and_save():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # ফাইলটির নাম হুবহু 'Mayapunjo_Final.m3u' হতে হবে
        with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_save()
