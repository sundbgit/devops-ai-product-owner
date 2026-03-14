import os
import requests
from dotenv import load_dotenv

load_dotenv()


class GitHubClient:

    def __init__(self):

        self.token = os.getenv("GITHUB_TOKEN")
        self.repo_owner = os.getenv("GITHUB_OWNER")
        self.repo_name = os.getenv("GITHUB_REPO")

        self.base_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}"

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

    def create_issue(self, title: str, body: str, labels=None):
        """
        Create a GitHub issue
        """

        url = f"{self.base_url}/issues"

        payload = {
            "title": title,
            "body": body,
            "labels": labels or []
        }

        response = requests.post(url, json=payload, headers=self.headers)

        if response.status_code == 201:
            issue = response.json()
            print(f"Created issue: {issue['html_url']}")
            return issue
        else:
            print("Failed to create issue")
            print(response.text)
            return None

    def create_issues_from_backlog(self, backlog: dict):
        """
        Create GitHub issues from AI generated backlog
        """

        epics = backlog.get("epics", [])

        for epic in epics:

            epic_title = epic["title"]

            for story in epic.get("stories", []):

                title = story["title"]

                description = story.get("description", "")

                tasks = story.get("tasks", [])

                body = f"""
### Epic
{epic_title}

### Description
{description}

### Tasks
"""

                for task in tasks:
                    body += f"- [ ] {task}\n"

                labels = ["story", story.get("priority", "medium").lower()]

                self.create_issue(title, body, labels)
