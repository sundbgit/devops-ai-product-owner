from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class AIService:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate_response(self, system_prompt: str, user_prompt: str, temperature: float = 0.2):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature
        )

        return response.choices[0].message.content
