<?php
// ১. আপনার কিনে আনা মূল ১২০ টাকার লিংকটি নিচে বসিয়ে দিন
$original_stream_url = "http://example.com/live/username/password/1234.m3u8"; 

// ফায়ারবেস বা অ্যাপ থেকে যদি ডাইনামিকালি লিংক পাঠাতে চান, তবে নিচের লাইনটি ব্যবহার করতে পারেন (ঐচ্ছিক)
if (isset($_GET['url'])) {
    $original_stream_url = urldecode($_GET['url']);
}

// ২. ভিডিও স্ট্রিমিংয়ের জন্য প্রয়োজনীয় হেডার সেট করা
header("Content-Type: video/mp4"); // আপনার সোর্স অনুযায়ী video/mp4 বা application/x-mpegURL হতে পারে
header("Cache-Control: no-cache, must-revalidate");
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT");

// ৩. টাইম আউট বন্ধ করা যাতে ভিডিও চলতে চলতে বন্ধ না হয়ে যায়
set_time_limit(0);

// ৪. মেইন সার্ভার থেকে কানেকশন ওপেন করে ডাটা রিড করা
$options = array(
    "http" => array(
        "header" => "User-Agent: VLC/3.0.8 LibVLC/3.0.8\r\n", // মেইন সার্ভারকে বোঝানো যে এটি একটি প্লেয়ার
        "method" => "GET"
    )
);
$context = stream_context_create($options);

// ৫. ডাটা রিড করে সরাসরি ইউজারের অ্যাপে আউটপুট দেওয়া (Chunk-by-Chunk)
$handle = fopen($original_stream_url, "rb", false, $context);
if ($handle) {
    while (!feof($handle) && connection_status() == 0) {
        echo fread($handle, 8192); // ৮ কেবি করে ডাটা বাফার করে পুশ করবে
        flush();
    }
    fclose($handle);
} else {
    header("HTTP/1.0 404 Not Found");
    echo "সোর্স লিংকটি কাজ করছে না!";
}
?>
