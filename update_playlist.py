import base64
import urllib.parse
import re
import requests

# ১. সঠিক হেডার কনফিগারেশন (যাতে লিঙ্কগুলো বন্ধ না হয়)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 12) ExoPlayerAdapter",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

def decode_and_verify(proxy_url):
    try:
        # লিঙ্ক থেকে এনকোড করা অংশ আলাদা করা
        if 'u=' in proxy_url:
            encoded_part = proxy_url.split('u=')[1]
            decoded_url = urllib.parse.unquote(encoded_part)
            
            # Base64 ডিকোড করা
            decoded_bytes = base64.b64decode(decoded_url)
            final_link = decoded_bytes.decode('utf-8')
            
            # এখানে আমরা চাইলে সরাসরি লিঙ্কটা রিটার্ন করতে পারি 
            # অথবা সার্ভার থেকে রিডাইরেক্ট হওয়া নতুন লিঙ্কটা নিতে পারি
            return final_link
        return proxy_url
    except Exception:
        return proxy_url

def create_vlc_playlist(input_file, output_file):
    print("--- মায়াপুঞ্জ টিভি: প্লে-লিস্ট তৈরি হচ্ছে ---")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # চ্যানেল নাম, লোগো এবং লিঙ্ক খুঁজে বের করা
    matches = re.findall(r'(#EXTINF:.*?,(.*?))\n(http.*)', content)
    
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write("#EXTM3U\n\n")
        
        for info, name, link in matches:
            channel_name = name.strip()
            # লিঙ্কটি পরিষ্কার ও ডিকোড করা
            clean_link = decode_and_verify(link.strip())
            
            f_out.write(f"{info}\n")
            f_out.write(f"{clean_link}\n\n")
            print(f"যোগ করা হয়েছে: {channel_name}")

    print(f"\nঅভিনন্দন! '{output_file}' ফাইলটি তৈরি হয়েছে।")
    print("এখন এটি VLC প্লেয়ারে ওপেন করে চেক করুন।")

# আপনার ফাইলের নাম 'Iptv.txt' থাকলে এটি রান করুন
create_vlc_playlist('Iptv.txt', 'Mayapunjo_Final.m3u')
