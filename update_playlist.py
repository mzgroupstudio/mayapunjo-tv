import requests

def fetch_playlist():
    # আপনার সংগৃহীত সোর্স ইউআরএল
    url = "http://paceitplaylists.geoclaster.xyz/m3u.php"
    
    # আপনার দেওয়া ছবির তথ্য অনুযায়ী হেডার
    headers = {
        'User-Agent': 'okhttp/4.12.0',
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Host': 'paceitplaylists.geoclaster.xyz'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            # সঠিক ফাইল নামে সেভ করা
            with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Playlist updated successfully!")
        else:
            print(f"Failed! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_playlist()
    
