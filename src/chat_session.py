class ChatSession:
    def __init__(self):
        self.latest_news = []

    def set_latest_news(self, news_list):
        self.latest_news = news_list

    def get_news_by_index(self, idx):
        if 0 <= idx < len(self.latest_news):
            return self.latest_news[idx]
        return None
