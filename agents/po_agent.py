import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


class ProductOwnerAgent:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def _build_prompt(self, meeting_notes: str) -> str:
        """
        Build the prompt that converts meeting notes into backlog items
        """

        prompt = f"""
You are an experienced Product Owner responsible for managing platform engineering backlogs.

Convert the following meeting discussion into:

- Epics
- Stories
- Tasks
- Priority (High/Medium/Low)

Return the result strictly in JSON format like this:

{{
  "epics": [
    {{
      "title": "Epic title",
      "description": "Epic description",
      "stories": [
        {{
          "title": "Story title",
          "description": "Story description",
          "priority": "High",
          "tasks": ["task1", "task2"]
        }}
      ]
    }}
  ]
}}

Meeting Notes:
{meeting_notes}
"""

        return prompt

    def generate_backlog(self, meeting_notes: str) -> dict:
        """
        Sends meeting notes to Azure OpenAI and returns structured backlog
        """

        prompt = self._build_prompt(meeting_notes)

        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {
                    "role": "system",
                    "content": "You are a platform product owner."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content

        try:
            backlog = json.loads(content)
        except json.JSONDecodeError:
            raise ValueError("AI response was not valid JSON")

        return backlog


if __name__ == "__main__":

    # simple local test

    with open("input/meeting_notes.md", "r") as f:
        notes = f.read()

    agent = ProductOwnerAgent()
    backlog = agent.generate_backlog(notes)

    print(json.dumps(backlog, indent=2))
