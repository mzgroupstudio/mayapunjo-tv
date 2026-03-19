import requests
import concurrent.futures

# এখানে প্রতিদিন আপনার নতুন লিঙ্কটি পেস্ট করবেন
source_url = "https://go.iptvpulse.top/34j8.m3u"

def check_link(stream_url):
    """লিঙ্কটি সচল কি না তা পরীক্ষা করার ফাংশন"""
    try:
        # ৫ সেকেন্ডের মধ্যে রেসপন্স না পেলে সেটি বাদ যাবে
        response = requests.head(stream_url, timeout=5, allow_redirects=True)
        if response.status_code == 200:
            return True
        # কিছু সার্ভার HEAD রিকোয়েস্ট সাপোর্ট করে না, তাই GET দিয়ে শেষ চেষ্টা
        response = requests.get(stream_url, timeout=5, stream=True)
        return response.status_code == 200
    except:
        return False

def update_and_filter():
    try:
        print(f"Downloading from: {source_url}")
        response = requests.get(source_url, timeout=30)
        lines = response.text.splitlines()
        
        channels_to_check = []
        for i in range(len(lines)):
            if lines[i].startswith("#EXTINF"):
                if i + 1 < len(lines):
                    channels_to_check.append({
                        'info': lines[i],
                        'url': lines[i+1].strip()
                    })

        active_content = ["#EXTM3U\n"]
        print(f"Total channels found: {len(channels_to_check)}. Checking status...")

        # দ্রুত চেক করার জন্য Multi-threading ব্যবহার করা হয়েছে
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_channel = {executor.submit(check_link, c['url']): c for c in channels_to_check}
            for future in concurrent.futures.as_completed(future_to_channel):
                channel = future_to_channel[future]
                if future.result():
                    active_content.append(channel['info'] + "\n")
                    active_content.append(channel['url'] + "\n")

        with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
            f.writelines(active_content)
        print("Success! Active channels saved in Mayapunjo_Final.m3u")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_and_filter()
