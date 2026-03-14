
import unittest
from services.backlog_service import BacklogService


sample_backlog = {
    "epics": [
        {
            "title": "AKS Cluster Upgrade",
            "description": "Upgrade AKS clusters to supported Kubernetes versions",
            "stories": [
                {
                    "title": "Upgrade development cluster",
                    "description": "Upgrade dev AKS cluster to Kubernetes 1.29",
                    "priority": "High",
                    "tasks": [
                        "Check deprecated APIs",
                        "Validate Helm charts",
                        "Upgrade node pools"
                    ]
                },
                {
                    "title": "Prepare production upgrade plan",
                    "description": "Create safe rollout plan for production cluster",
                    "priority": "Medium",
                    "tasks": [
                        "Document upgrade steps",
                        "Schedule maintenance window"
                    ]
                }
            ]
        }
    ]
}


class TestBacklogService(unittest.TestCase):

    def setUp(self):
        self.backlog_service = BacklogService(sample_backlog)

    def test_summary(self):
        summary = self.backlog_service.summary()

        self.assertEqual(summary["epic_count"], 1)
        self.assertEqual(summary["story_count"], 2)

    def test_get_epics(self):
        epics = self.backlog_service.get_epics()

        self.assertEqual(len(epics), 1)
        self.assertEqual(epics[0].title, "AKS Cluster Upgrade")

    def test_get_all_stories(self):
        stories = self.backlog_service.get_all_stories()

        self.assertEqual(len(stories), 2)
        self.assertEqual(stories[0]["title"], "Upgrade development cluster")
        self.assertEqual(stories[1]["priority"], "Medium")


if __name__ == "__main__":
    unittest.main()
