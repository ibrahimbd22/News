# News Patcher Bot

এটি একটি স্বয়ংক্রিয় টেলিগ্রাম বট, যা সাম্রাজ্যবাদ ও সামন্তবাদে নিপীড়িত দেশের শ্রমিক, কৃষক ও মেহনতী মানুষের লড়াইয়ের খবর সংগ্রহ করে টেলিগ্রাম চ্যানেলে পাঠায়।

---

## ফিচারসমূহ
- নির্দিষ্ট দেশগুলোর RSS ফিড থেকে প্রতিবাদ, ধর্মঘট, আন্দোলনের খবর সংগ্রহ।
- বাংলা ভাষায় সংক্ষিপ্ত সারাংশ তৈরি করা।
- টেলিগ্রাম চ্যানেলে অটোমেটিক মেসেজ পাঠানো।
- ফ্রি হোস্টিং সার্ভারে চালানো যায় (Railway/Render ইত্যাদিতে)।
- ইংরেজি থেকে বাংলা অনুবাদের সাপোর্ট (ভবিষ্যতের জন্য)।

---

## প্রয়োজনীয় ফাইলসমূহ
- `main.py` - খবর সংগ্রহ ও চ্যানেলে পাঠানোর মেইন স্ক্রিপ্ট।
- `send_message.py` - মেসেজ পাঠানোর ফাংশন।
- `config.py` - টোকেন, অ্যাডমিন আইডি ও চ্যানেল আইডি লোড করা।
- `utils.py` - টেক্সট প্রসেসিং ফাংশন।
- `translator.py` - ইংরেজি টু বাংলা অনুবাদ ফাংশন।
- `scraper.py` - ওয়েব স্ক্র্যাপিং ফাংশন (ভবিষ্যতের জন্য)।
- `sources.json` - দেশভিত্তিক RSS ফিডের তালিকা।
- `requirements.txt` - প্রয়োজনীয় প্যাকেজের তালিকা।
- `Procfile` - হোস্টিং সার্ভারের জন্য রান কমান্ড।
- `.env` - গোপন তথ্য রাখার লোকাল ফাইল (গিটহাবে আপলোড করবো না)।
- `.gitignore` - `.env` এবং cache ফাইল বাদ দেয়ার জন্য।

---

## কিভাবে চালাবেন (Deploy Instructions)

### Step 1: GitHub Repo তৈরি করুন
- সব ফাইল আপলোড করুন (except `.env`)

### Step 2: Railway বা Render এ ডিপ্লয় করুন
- **New Project > Deploy from GitHub Repo** করুন।
- Environment Variables এ নিচের তথ্য দিন:
  - `BOT_TOKEN` = আপনার টেলিগ্রাম বট টোকেন
  - `ADMIN_ID` = আপনার টেলিগ্রাম আইডি
  - `CHANNEL_ID` = আপনার টেলিগ্রাম চ্যানেলের username বা ID

### Step 3: Build এবং Start কমান্ড দিন
- **Build Command:**