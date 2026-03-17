import requests
import os

def fetch_playlist():
    # আপনার দেওয়া ছবির তথ্য অনুযায়ী
    url = "http://paceitplaylists.geoclaster.xyz/m3u.php"
    headers = {
        'User-Agent': 'okhttp/4.12.0',
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Host': 'paceitplaylists.geoclaster.xyz'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # প্লেলিস্টটি playlist.m3u নামে সেভ করবে
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Playlist updated successfully!")
        else:
            print(f"Failed to fetch. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_playlist()
  
