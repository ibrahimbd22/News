def clean_text(text):
    """
    টেক্সট ক্লিন করার ছোট ফাংশন।
    যেমন: অপ্রয়োজনীয় স্পেস, লাইন ব্রেক রিমুভ করা।
    """
    if text:
        return ' '.join(text.strip().split())
    return ''

def short_summary(text, limit=200):
    """
    বড় টেক্সট ছোট করে নির্দিষ্ট শব্দ সীমার মধ্যে এনে ফেলা।
    """
    if len(text) > limit:
        return text[:limit] + "..."
    return text