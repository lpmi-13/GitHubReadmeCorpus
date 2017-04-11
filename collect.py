from github import Github
import requests, base64, yaml

with open('settings.yaml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

g = Github(cfg['user'], cfg['password'], timeout=200, per_page=30)

'''
this call is the same as hitting the GitHub search API endpoint:
https://api.github.com/repositories, which yields every
publicly available repository on GitHub
'''
results = g.get_repos()

write_text = open('readmeText.txt', 'w')
write_text.truncate()

write_urls = open('urls.txt', 'w')
write_urls.truncate()

for repo in results:
    r = requests.get(repo.html_url)
    '''
    this check is just to make sure that the repo still
    exists. It might not be needed, though omitting this
    check has caused issues in past projects using the GitHub
    API, so leaving it in for now
    '''
    if r.headers.get('status') is not int(404):
        print 'processing README for ' + repo.html_url + '...'
        #writes each repository url to urls.txt
        write_urls.write(repo.html_url)
        write_urls.write('\n')

        try:
            readme = repo.get_readme() or ''
            data = base64.b64decode(readme.content)
        except:
            data = ''

        #writes the readme text, if it exists, to readmeText.txt
        write_text.write(data)
        write_text.write('\n\n')

print 'all done!'
