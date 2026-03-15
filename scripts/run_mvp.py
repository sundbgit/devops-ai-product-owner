import json
import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.po_agent import ProductOwnerAgent
from integrations.github_client import GitHubClient
from models.work_items import Backlog


def load_meeting_notes(file_path: str) -> str:
    """
    Read meeting notes from markdown file
    """
    with open(file_path, "r") as f:
        return f.read()


def main():

    print("\nDevOps AI Product Owner - MVP\n")

    meeting_notes_path = "input/meeting_notes.md"

    print("Loading meeting notes...")
    meeting_notes = load_meeting_notes(meeting_notes_path)

    print("Generating backlog using AI Product Owner...")

    agent = ProductOwnerAgent()
    backlog_data = agent.generate_backlog(meeting_notes)

    print("\nRaw AI Output:\n")
    print(json.dumps(backlog_data, indent=2))

    print("\nValidating backlog structure...")

    backlog = Backlog(**backlog_data)

    print(f"\nEpics generated: {len(backlog.epics)}")

    for epic in backlog.epics:
        print(f" - {epic.title} ({len(epic.stories)} stories)")

    print("\nCreating GitHub issues...")

    github = GitHubClient()
    github.create_issues_from_backlog(backlog_data)

    print("\nMVP pipeline completed successfully\n")


if __name__ == "__main__":
    main()
