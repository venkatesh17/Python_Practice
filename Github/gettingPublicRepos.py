import base64
from github import Github
from pprint import pprint

username = "venkatesh17"

g= Github()

user = g.get_user()

for repo in user.get_repos():
    print(repo)

    