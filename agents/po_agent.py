from services.ai_service import AIService
import json

class ProductOwnerAgent:

    def __init__(self):
        self.ai_service = AIService()

    def _build_prompt(self, meeting_notes: str) -> str:

        with open("prompts/backlog_prompt.txt", "r") as f:
            template = f.read()

        return template.replace("{{MEETING_NOTES}}", meeting_notes)

    def generate_backlog(self, meeting_notes: str) -> dict:

        prompt = self._build_prompt(meeting_notes)

        response = self.ai_service.generate_response(
            system_prompt="You are a DevOps platform product owner.",
            user_prompt=prompt
        )

        try:
            backlog = json.loads(response)
        except json.JSONDecodeError:
            print("\nRaw AI Response:\n", response)
            raise ValueError("AI response was not valid JSON")

        return backlog
