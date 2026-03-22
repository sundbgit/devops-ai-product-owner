# devops-ai-product-owner
An AI-powered Product Owner agent for DevOps platform teams that converts technical discussions into sprint backlogs, stories, and standup summaries using LLMs.

# Usage
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

sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % python3 -m venv venv
sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % source venv/bin/activate
(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % date
Sun Mar 22 12:21:01 IST 2026
(venv) sunilpoojary@Sunils-MacBook-Air devops-ai-product-owner % 
~~~

~~~
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

After the basic setup, add an Open API key in the .env file and the model name. 

The .env should look like. DO not check in to github. use .gitignore 

~~~
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
OPENAI_MODEL=gpt-4o-mini
~~~

To create Open API key - Navigate to https://platform.openai.com/ and Create new secret key. Keep the details as default and permissions as default which we can change later. PLease add billing details with as low as 5$ for the basic tests. We can add once you need more :)


