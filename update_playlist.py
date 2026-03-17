import requests

def fetch_playlist():
    # ছবির নতুন ইউআরএল (পুরোটা কপি করে এখানে বসাবেন)
    url = "http://172.19.178.182/playlist/index.php?encryptedData=..." # আপনার ছবির পুরো লিঙ্কটি এখানে দিন
    
    headers = {
        'User-Agent': 'Mozila', # ছবিতে যা আছে হুবহু তাই (Mozilla বানানে একটি 'l' কম আছে ছবিতে)
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Host': '172.19.178.182'
    }

    try:
        # যেহেতু এটি লোকাল আইপি, গিটহাব থেকে এটি কাজ করার সম্ভাবনা কম
        # যদি এটি কোনো ভিপিএন বা লোকাল নেটওয়ার্কের হয়, তবে এটি আপনার পিসিতে রান করা ভালো
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            with open("Mayapunjo_Final.m3u", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Success!")
        else:
            print(f"Failed with status: {response.status_code}")
    except Exception as e:
        print(f"Error connecting: {e}")

if __name__ == "__main__":
    fetch_playlist()
