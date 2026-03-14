
from models.work_items import Backlog, Epic, Story


class BacklogService:
    """
    Handles backlog processing and transformation
    """

    def __init__(self, backlog_data: dict):

        self.backlog = Backlog(**backlog_data)

    def get_epics(self):
        """
        Return list of epics
        """
        return self.backlog.epics

    def get_all_stories(self):
        """
        Flatten stories across all epics
        """
        stories = []

        for epic in self.backlog.epics:
            for story in epic.stories:
                stories.append({
                    "epic": epic.title,
                    "title": story.title,
                    "description": story.description,
                    "priority": story.priority,
                    "tasks": story.tasks
                })

        return stories

    def summary(self):
        """
        Print a backlog summary
        """

        summary = {
            "epic_count": len(self.backlog.epics),
            "story_count": sum(len(epic.stories) for epic in self.backlog.epics)
        }

        return summary

    def print_backlog(self):
        """
        Pretty print backlog
        """

        for epic in self.backlog.epics:

            print(f"\nEpic: {epic.title}")

            for story in epic.stories:

                print(f"  Story: {story.title}")
                print(f"  Priority: {story.priority}")

                for task in story.tasks:
                    print(f"     - {task}")
