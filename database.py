import sqlite3
from config import DATABASE_NAME

def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT UNIQUE,
            summary TEXT,
            source TEXT,
            published TEXT,
            date_saved TEXT,
            was_sent INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    print("Database ready")

def save_articles(articles):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    saved_count = 0
    skipped_count = 0

    for article in articles:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO articles 
                (title, link, summary, source, published, date_saved)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
            """, (
                article["title"],
                article["link"],
                article["summary"],
                article["source"],
                article["published"]
            ))
            if cursor.rowcount > 0:
                saved_count += 1
            else:
                skipped_count += 1
        except sqlite3.Error as e:
            print(f" DB Error: {e}")

    conn.commit()
    conn.close()
    print(f" Saved: {saved_count} new | Skipped: {skipped_count} duplicates")

def get_unsent_articles(limit=15):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, link, summary, source
        FROM articles
        WHERE was_sent = 0
        ORDER BY date_saved DESC
        LIMIT ?
    """, (limit,))
    articles = cursor.fetchall()
    conn.close()
    return [
        {"id": row[0], "title": row[1], "link": row[2],
         "summary": row[3], "source": row[4]}
        for row in articles
    ]

def mark_articles_sent(article_ids):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    placeholders = ",".join("?" * len(article_ids))
    cursor.execute(f"""
        UPDATE articles SET was_sent = 1 
        WHERE id IN ({placeholders})
    """, article_ids)
    conn.commit()
    conn.close()
    print(f" Marked {len(article_ids)} articles as sent")

def get_stats():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM articles")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM articles WHERE was_sent = 1")
    sent = cursor.fetchone()[0]
    cursor.execute("""
        SELECT source, COUNT(*) as count 
        FROM articles 
        GROUP BY source 
        ORDER BY count DESC
    """)
    by_source = cursor.fetchall()
    conn.close()
    print(f"\n DATABASE STATS:")
    print(f"Total articles: {total}")
    print(f"Sent: {sent} | Pending: {total - sent}")
    print(f"\nBy Source:")
    for source, count in by_source:
        print(f"  {source}: {count} articles")

if __name__ == "__main__":
    create_database()
    get_stats()