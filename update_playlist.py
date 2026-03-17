import requests
import re

# আপনার সোর্স লিঙ্ক
url = "http://paceitplaylists.geoclaster.xyz/m3u.php"
headers = {
    "User-Agent": "okhttp/4.12.0",
}

def fetch_and_save():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        content = response.text
        
        # ১. .m3u ফাইল সেভ করা
        with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
            f.write(content)
        print("M3U File Updated Successfully")

        # ২. ফাইল থেকে একটি চ্যানেলের লিঙ্ক খুঁজে বের করা (উদাহরণ: প্রথম .m3u8 লিঙ্কটি)
        # আপনি চাইলে নির্দিষ্ট কোনো চ্যানেলের নাম দিয়েও ফিল্টার করতে পারেন
        links = re.findall(r'(http[s]?://[^\s]+)', content)
        video_url = ""
        for link in links:
            if ".m3u8" in link or "proxy.php" in link:
                video_url = link
                break

        # ৩. HTML প্লেয়ার ফাইল তৈরি করা
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
    <video id="my-video" class="video-js vjs-big-play-centered" controls preload="auto" data-setup='{{"autoplay": true, "muted": false}}'>
        <source src="{video_url}" type="application/x-mpegURL">
    </video>
    <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
</body>
</html>
"""
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            print("Index.html Player Created Successfully")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_save()
