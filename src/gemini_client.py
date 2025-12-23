import google.generativeai as genai
import json, re

class GeminiClient:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def _extract_json(self, text: str):
        """
        Tách JSON ra khỏi output của model.
        Hỗ trợ cả block ```json ... ``` hoặc JSON trần.
        """
        # 1️⃣ Tìm trong ```json ... ```
        match = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", text)
        if match:
            json_str = match.group(1)
        else:
            # 2️⃣ Nếu không có, tìm khối {...}
            match = re.search(r"\{[\s\S]*\}", text)
            json_str = match.group(0) if match else None

        if not json_str:
            return {"intent": "chat", "parameters": {}}

        # 3️⃣ Parse JSON an toàn
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return {"intent": "chat", "parameters": {}}
        
    def analyze_intent(self, user_input: str, context: dict):
        prompt = f"""
        Bạn là chatbot đọc tin tức.
        Hãy đọc câu sau và xác định hành động cần làm.
        - Nếu user hỏi xem tin hôm nay -> intent = "get_latest_news"
        - Nếu user nói 'tóm tắt tin số ...' -> intent = "read_news" + index.
        - Nếu không thì intent = "chat"

        Trả về JSON dạng:
        {{
            "intent": "...",
            "parameters": {{}}
        }}

        User: "{user_input}"
        Context: {context}
        """

        response = self.model.generate_content(prompt)
        text = response.text.strip()
        data = self._extract_json(text)
        return data["intent"], data.get("parameters", {})
    
        
    def ask(self, user_input: str, context: dict):
        prompt = f"""
        Bạn là chatbot đọc tin tức.
        Hãy đọc câu sau và xác định hành động cần làm.
        - Nếu user hỏi xem tin hôm nay -> intent = "get_latest_news"
        - Nếu user nói 'tóm tắt tin số ...' -> intent = "read_news" + index.
        - Nếu không thì intent = "chat"

        Trả về JSON dạng:
        {{
            "intent": "...",
            "parameters": {{}}
        }}

        User: "{user_input}"
        Context: {context}
        """

        response = self.model.generate_content(prompt)
        text = response.text.strip()
        data = self._extract_json(text)
        return data["intent"], data.get("parameters", {})
    