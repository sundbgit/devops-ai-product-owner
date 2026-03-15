
import json
import yaml
from services.ai_service import AIService


class SprintService:
    """
    Service responsible for generating sprint plans from backlog
    """

    def __init__(self):

        self.ai_service = AIService()

        # Load configuration
        with open("config/settings.yaml", "r") as f:
            self.settings = yaml.safe_load(f)

        # Load prompt template
        with open("prompts/sprint_prompt.txt", "r") as f:
            self.prompt_template = f.read()

    def _build_prompt(self, backlog: dict):
        """
        Inject backlog and team information into the prompt
        """

        team_size = self.settings["team"]["team_size"]
        sprint_length = self.settings["team"]["sprint_length_days"]

        prompt = self.prompt_template.replace("{{TEAM_SIZE}}", str(team_size))
        prompt = prompt.replace("{{SPRINT_LENGTH}}", str(sprint_length))
        prompt = prompt.replace("{{BACKLOG}}", json.dumps(backlog, indent=2))

        return prompt

    def generate_sprint_plan(self, backlog: dict):
        """
        Generate sprint plan using AI
        """

        prompt = self._build_prompt(backlog)

        response = self.ai_service.generate_response(
            system_prompt="You are a DevOps platform product owner responsible for sprint planning.",
            user_prompt=prompt
        )

        try:
            sprint_plan = json.loads(response)
        except json.JSONDecodeError:
            raise ValueError("Sprint plan response was not valid JSON")

        return sprint_plan
