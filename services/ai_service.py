
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


class AIService:
    """
    Handles interaction with Azure OpenAI
    """

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def generate_response(self, system_prompt: str, user_prompt: str, temperature: float = 0.2):
        """
        Send prompt to Azure OpenAI and return response
        """

        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=temperature
        )

        return response.choices[0].message.content
