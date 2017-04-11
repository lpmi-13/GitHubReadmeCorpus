from github import Github
import requests, base64, re, yaml

with open('settings.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

g = Github(cfg['user'], cfg['password'], timeout=200, per_page=30)

results = g.get_repos()

for repo in results:
    print repo.html_url

    readme = repo.get_readme()
    data = base64.b64decode(readme.content)

    print '###################'
    print 
