import requests
from bs4 import BeautifulSoup

def simple_scrape(url):
    """
    নির্দিষ্ট একটা URL থেকে শিরোনাম (title) ও প্যারা (p) টেক্সট স্ক্র্যাপ করা।
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('title').text if soup.find('title') else 'No Title Found'
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])

        return {
            'title': title,
            'content': content[:1000]  # প্রথম ১০০০ অক্ষর
        }
    except Exception as e:
        print(f"Scraping Error: {e}")
        return None