import feedparser
from datetime import datetime, timedelta
from config import RSS_FEEDS

def fetch_articles():
    all_articles = []
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    for feed_url in RSS_FEEDS:
        print(f" Fetching from: {feed_url}")
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:20]:
            pub_date = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                pub_date = datetime(*entry.published_parsed[:6]).date()
            elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                pub_date = datetime(*entry.updated_parsed[:6]).date()

            if pub_date is None:
                continue
            if pub_date < yesterday:
                continue

            article = {
                "title": entry.get("title", "No title"),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", "")[:300],
                "source": feed.feed.get("title", "Unknown Source"),
                "published": str(pub_date)
            }
            all_articles.append(article)

    print(f" Found {len(all_articles)} articles from today/yesterday")
    return all_articles

if __name__ == "__main__":
    articles = fetch_articles()
    for i, article in enumerate(articles[:5]):
        print(f"\n--- Article {i+1} ---")
        print(f"Title: {article['title']}")
        print(f"Published: {article['published']}")
        print(f"Source: {article['source']}")