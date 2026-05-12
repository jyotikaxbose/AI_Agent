# config.py
import os
from dotenv import load_dotenv

# Load keys from .env file
load_dotenv()

# API KEYS — loaded from .env file (never hardcoded)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# NEWS SOURCES
RSS_FEEDS = [
    "https://techcrunch.com/tag/artificial-intelligence/feed/",
    "https://www.artificialintelligence-news.com/feed/",
    "https://aiweekly.co/issues.rss",
    "https://thenextweb.com/neural/feed/",
    "https://huggingface.co/blog/feed.xml",
    "https://openai.com/blog/rss/",
    "https://deepmind.google/blog/rss/",
    "https://blogs.microsoft.com/ai/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://www.wired.com/feed/tag/artificial-intelligence/rss",
]

DATABASE_NAME = "ai_news.db"
DAILY_TIME = "08:00"