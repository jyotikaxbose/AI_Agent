from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def summarize_articles(articles):
    if not articles:
        print("No articles to summarize")
        return None

    articles_text = ""
    for i, article in enumerate(articles):
        articles_text += f"""
Article {i+1}:
Title: {article['title']}
Source: {article['source']}
Summary: {article['summary']}
Link: {article['link']}
---"""

    prompt = f"""You are an AI news curator. Here are today's AI news articles:

{articles_text}

Pick the TOP 5 most important stories and write a daily digest in this format:

 Daily AI News Digest

1. [Article Title]
[2-sentence summary in simple English]
Link: [link]

2. [Article Title]
[2-sentence summary]
Link: [link]

(continue for all 5)

---
Your daily AI digest | Powered by AI"""

    print("Asking Groq to summarize...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    print("Summary ready")
    return response.choices[0].message.content

if __name__ == "__main__":
    test_articles = [
        {"title": "OpenAI releases GPT-5", "source": "TechCrunch",
         "summary": "OpenAI has released GPT-5 with major improvements.",
         "link": "https://techcrunch.com/test1"},
        {"title": "Google Gemini beats benchmarks", "source": "AI News",
         "summary": "Google Gemini surpassed all competitors.",
         "link": "https://ainews.com/test2"},
    ]
    result = summarize_articles(test_articles)
    print(result)