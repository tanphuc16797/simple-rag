from news import get_latest_news, read_news
from chat_session import ChatSession
from gemini_client import GeminiClient
from rag_memory import RAGMemory
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
RSS_FEED = os.getenv("RSS_FEED")

gemini = GeminiClient(API_KEY)
session = ChatSession()
rag = RAGMemory()

def handle_user(user_input: str):
    context = {"latest_news": session.latest_news}
    intent, params = gemini.analyze_intent(user_input, context)

    if intent == "get_latest_news":
        news_list = get_latest_news(RSS_FEED, limit=5)
        session.set_latest_news(news_list)
        return "Hôm nay có những tin:\n" + "\n".join(f"{i+1}. {n['title']}" for i, n in enumerate(news_list))

    elif intent == "read_news":
        idx = int(params.get("index", 1)) - 1
        news_item = session.get_latest_news(idx)
        if news_item:
            content = read_news(news_item["link"])
            rag.add(content)
            return gemini.ask(user_input, f"Tóm tắt tin {idx+1}:\n{content}...")
        return "Tin không tồn tại."

    elif intent == "chat":
        idx = int(params.get("index", 1)) - 1
        news_item = session.get_latest_news(idx)
        if news_item:
            content = read_news(news_item["link"])
            rag.add(content)
            return gemini.ask(user_input, f"Tóm tắt tin {idx+1}:\n{content}...")
        return "Tin không tồn tại."

    else:
        retrieved = rag.retrieve(user_input)
        if retrieved:
            return gemini.ask(user_input, f"Dựa trên tin đã lưu: {retrieved[0]}")
        return gemini.ask(user_input, f"Mình không tìm thấy thông tin liên quan.")

# Demo chat loop
while True:
    user_input = input("User: ")
    print("Bot:", handle_user(user_input))

