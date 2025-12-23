import feedparser
import requests
from bs4 import BeautifulSoup

def get_latest_news(feed_url: str, limit: int = 5):
    feed = feedparser.parse(feed_url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({
            "title": entry.title,
            "link": entry.link,
            "summary": getattr(entry, "summary", "")
        })
    return items

def read_news(link: str):
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        content = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        return content
    except Exception as e:
        return f"Không thể lấy nội dung: {e}"

