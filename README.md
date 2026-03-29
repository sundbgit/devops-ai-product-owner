# devops-ai-product-owner
An AI-powered Product Owner agent for DevOps platform teams that converts meeting discussions into structured backlog items, epics, and sprint-ready stories.

# Problem Statement

DevOps/platform teams often:
1. Don’t have a traditional Product Owner
2. Spend time manually converting discussions into tasks
3. Lose context from meetings
4. Struggle with backlog prioritization

# Solution

This project introduces an AI Product Owner Agent that:
1. Converts meeting notes → Epics, Stories, Tasks
2. Structures backlog using DevOps best practices
3. Automatically creates GitHub issues
4. Lays foundation for sprint planning automation

# Architecture

Meeting Notes (Teams / Markdown)
        ↓
ProductOwnerAgent
        ↓
AI Service (OpenAI)
        ↓
Backlog (Pydantic Validation)
        ↓
GitHub Integration
        ↓
Issues Created Automatically
  
# Tech Stack

1. Python
2. OpenAI API
3. Pydantic
4. GitHub API
5. YAML Config

# Demo


# Quick Start

1. Clone Repo
~~~
sunilpoojary@Sunils-MacBook-Air ~ % mkdir devops-product-owner
sunilpoojary@Sunils-MacBook-Air ~ % cd devops-product-owner 
sunilpoojary@Sunils-MacBook-Air devops-product-owner % git clone https://github.com/sundbgit/devops-ai-product-owner.git
Cloning into 'devops-ai-product-owner'...
remote: Enumerating objects: 100, done.
remote: Counting objects: 100% (100/100), done.
remote: Compressing objects: 100% (83/83), done.
remote: Total 100 (delta 32), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (100/100), 35.20 KiB | 3.20 MiB/s, done.
Resolving deltas: 100% (32/32), done.
sunilpoojary@Sunils-MacBook-Air devops-product-owner % cd devops-ai-product-owner                                          
sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % ls
agents			input			models			README.md		scripts			tests
config			integrations		prompts			requirements.txt	services
sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner %
~~~

2. Setup Virtual Environment
~~~
sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % python3 -m venv venv
sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % source venv/bin/activate
(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % date
Sun Mar 22 12:21:01 IST 2026
(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % 
(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % pip install -r requirements.txt
Collecting openai>=1.30.0
  Downloading openai-2.29.0-py3-none-any.whl (1.1 MB)
     |████████████████████████████████| 1.1 MB 615 kB/s 
Collecting python-dotenv>=1.0.1

(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Downloading pip-26.0.1-py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 1.0 MB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-26.0.1
(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % 

~~~

3. Configure .env

The .env should look like. Do not check in to github. use .gitignore 

~~~
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
OPENAI_MODEL=gpt-4o-mini
GITHUB_TOKEN=Pat token which has issues( read and write permisssion) and metadata (read permission)
GITHUB_OWNER=Provide your username
GITHUB_REPO=Provide your repo name
~~~

To create Open API key - Navigate to https://platform.openai.com/ and create new secret key. Keep the details as default and permissions as default which we can change later. Please add billing details with as low as 5$ for the basic tests. We can add once you need more :)

4. Run the Application

~~~

(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % python scripts/run_mvp.py
/Users/sunilpoojary/devops-product-owner/devops-ai-product-owner/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

DevOps AI Product Owner - MVP

Loading meeting notes...
Generating backlog using AI Product Owner...

Raw AI Output:

{
  "epics": [
    {
      "title": "AKS Upgrade",
      "description": "Upgrade the AKS cluster to the latest Kubernetes version to ensure compliance and support.",
      "stories": [
        {
          "title": "Plan AKS Cluster Upgrade Strategy",
          "description": "Develop a detailed plan for upgrading the AKS cluster from version 1.31 to 1.32, including timelines and resource allocation.",
          "priority": "High",
          "tasks": [
            "Review Microsoft deprecation timelines",
            "Identify application compatibility requirements",
            "Draft upgrade strategy document"
          ]
        },
        {
          "title": "Verify Application Compatibility",
          "description": "Ensure that all applications running on the AKS cluster are compatible with Kubernetes version 1.32.",
          "priority": "High",
          "tasks": [
            "Run compatibility tests on all applications",
            "Document any compatibility issues",
            "Coordinate with application teams for fixes"
          ]
        },
        {
          "title": "Review Helm Charts for Deprecated APIs",
          "description": "Audit existing Helm charts for deprecated APIs that may affect the upgrade process.",
          "priority": "Medium",
          "tasks": [
            "List all Helm charts in use",
            "Identify deprecated APIs in each chart",
            "Update Helm charts to remove deprecated APIs"
          ]
        },
        {
          "title": "Test Upgrade Process in Development Environment",
          "description": "Conduct a test upgrade of the AKS cluster in a development environment to validate the upgrade process.",
          "priority": "High",
          "tasks": [
            "Set up a development AKS cluster",
            "Perform the upgrade to version 1.32",
            "Document the upgrade process and any issues encountered"
          ]
        }
      ]
    },
    {
      "title": "CI Pipeline Stability",
      "description": "Improve the stability of CI pipelines to reduce failures and enhance developer productivity.",
      "stories": [
        {
          "title": "Investigate Flaky CI Tests",
          "description": "Analyze the CI pipeline to identify and resolve flaky integration tests causing intermittent failures.",
          "priority": "High",
          "tasks": [
            "Run test reports to identify flaky tests",
            "Review test code for potential issues",
            "Refactor or rewrite flaky tests"
          ]
        },
        {
          "title": "Improve Pipeline Retry Logic",
          "description": "Enhance the retry logic in CI pipelines to handle transient failures more effectively.",
          "priority": "Medium",
          "tasks": [
            "Review current retry logic implementation",
            "Implement exponential backoff strategy",
            "Test new retry logic in CI environment"
          ]
        },
        {
          "title": "Stabilize CI Workflow",
          "description": "Make necessary adjustments to the CI workflow to ensure consistent execution and reliability.",
          "priority": "Medium",
          "tasks": [
            "Review CI workflow configurations",
            "Identify bottlenecks in the workflow",
            "Implement improvements based on findings"
          ]
        }
      ]
    },
    {
      "title": "Infrastructure as Code Refactoring",
      "description": "Refactor Terraform modules to enhance maintainability and usability.",
      "stories": [
        {
          "title": "Refactor Terraform Networking Modules",
          "description": "Simplify and improve the existing Terraform modules used for networking infrastructure.",
          "priority": "High",
          "tasks": [
            "Review current networking module structure",
            "Implement modular design principles",
            "Update documentation for new module structure"
          ]
        },
        {
          "title": "Refactor Terraform AKS Infrastructure Modules",
          "description": "Refactor the Terraform modules used for provisioning AKS infrastructure to improve readability and reuse.",
          "priority": "High",
          "tasks": [
            "Analyze existing AKS modules for complexity",
            "Introduce variable validation for inputs",
            "Create comprehensive documentation for modules"
          ]
        }
      ]
    },
    {
      "title": "Monitoring and Observability Improvements",
      "description": "Enhance monitoring configurations to reduce alert noise and improve actionable insights.",
      "stories": [
        {
          "title": "Review Monitoring Alert Thresholds",
          "description": "Assess and adjust alert thresholds to minimize excessive alerts and focus on actionable notifications.",
          "priority": "High",
          "tasks": [
            "Compile list of current alert thresholds",
            "Analyze alert frequency and impact",
            "Adjust thresholds based on analysis"
          ]
        },
        {
          "title": "Remove Redundant Alerts",
          "description": "Identify and eliminate redundant alerts from the monitoring system to reduce alert fatigue.",
          "priority": "Medium",
          "tasks": [
            "Review all active alerts",
            "Identify alerts that overlap or provide no value",
            "Document and remove redundant alerts"
          ]
        },
        {
          "title": "Introduce Better Severity Classifications",
          "description": "Implement a more effective classification system for alerts to prioritize response efforts.",
          "priority": "Medium",
          "tasks": [
            "Define severity levels for alerts",
            "Update monitoring configurations with new classifications",
            "Train team on new alert severity system"
          ]
        }
      ]
    }
  ]
}

Validating backlog structure...

Epics generated: 4
 - AKS Upgrade (4 stories)
 - CI Pipeline Stability (3 stories)
 - Infrastructure as Code Refactoring (2 stories)
 - Monitoring and Observability Improvements (3 stories)

Creating GitHub issues...
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/3
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/4
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/5
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/6
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/7
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/8
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/9
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/10
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/11
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/12
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/13
Created issue: https://github.com/sundbgit/devops-ai-product-owner/issues/14

MVP pipeline completed successfully

(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % 

~~~

5. Validate the issues in Github.
   
<img width="1434" height="753" alt="Screenshot 2026-03-22 at 1 55 44 PM" src="https://github.com/user-attachments/assets/3bdfe30c-add1-4607-ba70-911969566857" />


6. Cost Efficiency

* Model: gpt-4o-mini
* Cost per run: <$0.01
* Suitable for frequent DevOps workflows

