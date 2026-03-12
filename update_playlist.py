import requests

# আপনার সেই সোর্স লিংক এবং হেডার
url = "http://paceitplaylists.geoclaster.xyz/m3u.php"
headers = {
    "User-Agent": "okhttp/4.12.0",
    "Host": "paceitplaylists.geoclaster.xyz"
}

def fetch_and_save():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_status == 200:
            with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("প্লেলিস্ট সফলভাবে আপডেট হয়েছে!")
        else:
            print("সার্ভার থেকে ডাটা পাওয়া যায়নি।")
    except Exception as e:
        print(f"ভুল হয়েছে: {e}")

if __name__ == "__main__":
    fetch_and_save()
