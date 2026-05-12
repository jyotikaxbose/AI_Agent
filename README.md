# AI News Agent 🤖

An automated AI news aggregation agent built in Python that scrapes, 
summarizes, and delivers daily AI news to Telegram.

## What it does
- Scrapes 10 AI news sources (TechCrunch, VentureBeat, HuggingFace, OpenAI blog and more)
- Filters only today's and yesterday's articles
- Stores and deduplicates articles using SQLite database
- Summarizes top 5 stories using Groq LLaMA AI
- Delivers a formatted daily digest to Telegram automatically every morning

## Tech Stack
- Python 3.13
- SQLite (database layer)
- Groq API / LLaMA 3.3 (AI summarization)
- Telegram Bot API (delivery)
- feedparser (RSS scraping)
- python-dotenv (secure credential management)

## Project Structure
ai_news_agent/
├── config.py          # Settings & environment variables
├── scraper.py         # RSS feed scraping & date filtering
├── database.py        # SQLite CRUD operations
├── summarizer.py      # Groq AI summarization
├── telegram_bot.py    # Telegram Bot API delivery
├── main.py            # Pipeline orchestration
└── scheduler.py       # Daily automation

## Key Features
- **Deduplication** — same article never saved or sent twice
- **Date filtering** — only today's/yesterday's news delivered
- **Secure credentials** — API keys managed via environment variables
- **Modular design** — each component independently testable

## Setup

1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file with your keys:
GROQ_API_KEY=your_key
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
6. Run: `python main.py`

## Skills Demonstrated
- Python automation & API integration
- SQL database design (CREATE, INSERT, SELECT, UPDATE)
- REST API consumption (Groq, Telegram)
- Secure credential management
- Modular software architecture