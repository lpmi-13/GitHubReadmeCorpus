from github import Github
import requests, base64, re, yaml

with open('settings.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

g = GitHub(cfg['user'], cfg['password'], timeout=200, per_page=30)

results = g.get_repos()

for repo in results:
    print repo.html_url
