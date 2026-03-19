import requests

url = "https://go.iptvpulse.top/34j8.m3u"
# এখানে আমরা একটি সাধারণ আইপিটিভি প্লেয়ারের পরিচয় দিচ্ছি
headers = {
    'User-Agent': 'VLC/3.0.18 LibVLC/3.0.18'
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open("playlist_output.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("সফলভাবে ফাইলটি সেভ হয়েছে! 'playlist_output.txt' চেক করুন।")
    else:
        print(f"Error: {response.status_code}. সার্ভার এখনও ব্লক করছে।")
except Exception as e:
    print(f"An error occurred: {e}")
