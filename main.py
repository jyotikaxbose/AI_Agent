from scraper import fetch_articles
from database import create_database, save_articles, get_unsent_articles, mark_articles_sent, get_stats
from summarizer import summarize_articles
from telegram_bot import send_telegram_message

def run_agent():
    print("\n" + "="*50)
    print("AI NEWS AGENT STARTING")
    print("="*50)

    create_database()
    articles = fetch_articles()
    save_articles(articles)

    unsent = get_unsent_articles(limit=15)
    print(f" {len(unsent)} unsent articles found")

    if not unsent:
        print("No new articles to send today")
        return

    summary = summarize_articles(unsent)

    if not summary:
        print("Summarization failed")
        return

    success = send_telegram_message(summary)

    if success:
        article_ids = [a["id"] for a in unsent]
        mark_articles_sent(article_ids)

    get_stats()
    print("\n AGENT RUN COMPLETE")

if __name__ == "__main__":
    run_agent()