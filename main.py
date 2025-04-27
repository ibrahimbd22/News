import json
import feedparser
from send_message import send_message

# sources.json ফাইল থেকে সোর্স লোড করা
with open('sources.json', 'r', encoding='utf-8') as f:
    sources = json.load(f)

def fetch_news():
    all_news = {}

    for country, urls in sources.items():
        news_list = []
        print(f"Fetching news for {country}...")

        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:  # প্রতিটি সাইট থেকে ৫টি করে খবর
                news_item = {
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published if 'published' in entry else 'No date'
                }
                news_list.append(news_item)

                # টেলিগ্রাম চ্যানেলে মেসেজ পাঠানো
                message = f"দেশ: {country}\nশিরোনাম: {entry.title}\nলিঙ্ক: {entry.link}"
                send_message(message)

        all_news[country] = news_list

    # ফাইল হিসেবে সংরক্ষণ করা
    with open('all_news.json', 'w', encoding='utf-8') as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)

    print("All news fetched, saved and sent to Telegram!")

if __name__ == "__main__":
    fetch_news()