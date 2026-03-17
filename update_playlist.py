import requests
import re

# আপনার মেইন প্লেলিস্ট লিঙ্ক
url = "http://paceitplaylists.geoclaster.xyz/m3u.php"
headers = {
    "User-Agent": "okhttp/4.12.0",
}

def fetch_and_save():
    try:
        # ১. প্লেলিস্ট ডাউনলোড করা
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        content = response.text
        
        # ২. Mayapunjo_Final.m3u ফাইল হিসেবে সেভ করা
        with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("M3U File Updated")

        # ৩. কন্টেন্ট থেকে ভিডিও লিঙ্ক (m3u8 বা proxy) খুঁজে বের করা
        # এখানে প্রথম লিঙ্কটি নেওয়া হচ্ছে, আপনি চাইলে নির্দিষ্ট নাম দিয়েও ফিল্টার করতে পারেন
        links = re.findall(r'(http[s]?://[^\s]+)', content)
        video_url = ""
        for link in links:
            if ".m3u8" in link or "proxy.php" in link:
                video_url = link
                break

        # ৪. যদি ভিডিও লিঙ্ক পাওয়া যায়, তবে index.html প্লেয়ার তৈরি করা
        if video_url:
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mayapunjo TV Player</title>
    <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
    <style>
        body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; background: #000; overflow: hidden; display: flex; justify-content: center; align-items: center; }}
        .video-js {{ width: 100% !important; height: 100% !important; }}
    </style>
</head>
<body>
    <video id="my-video" class="video-js vjs-big-play-centered" controls autoplay preload="auto" data-setup='{{"fluid": true}}'>
        <source src="{video_url}" type="application/x-mpegURL">
    </video>
    <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
</body>
</html>
"""
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            print("index.html (Player) Updated")
        else:
            print("No video link found to create player")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_save()
