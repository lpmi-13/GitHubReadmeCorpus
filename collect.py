from github import Github
import requests, base64
import csv
import os
from process import process_id


SAVE_DIRECTORY = 'data/'
highest_repo_id = 0

for fn in os.listdir(SAVE_DIRECTORY):
    if int(process_id(fn)) > highest_repo_id:
        highest_repo_id = int(process_id(fn))


g = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'], timeout=200, per_page=30)

'''
this call is the same as hitting the GitHub search API endpoint:
https://api.github.com/repositories, which yields every
publicly available repository on GitHub
'''

print 'highest repo id is ' + str(highest_repo_id)

results = g.get_repos(since=highest_repo_id)


for repo in results:
    print ('processing {}').format(repo.id)

    response = requests.get(repo.html_url)
    '''
    this check is just to make sure that the repo still
    exists. It might not be needed, though omitting this
    check has caused issues in past projects using the GitHub
    API, so leaving it in for now
    '''
    if response.headers.get('status') is not int(404):
        print 'processing README for ' + repo.html_url + '...'

        try:
            readme = repo.get_readme() or ''
            data = base64.b64decode(readme.content)
        except:
            data = ''

        #writes the readme text, if it exists, to a csv file 
        filename = 'repo-{}.csv'.format(repo.id)
        path_to_file = SAVE_DIRECTORY + filename

        clean_data = data.replace('\n', '')

        with open(path_to_file, 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', escapechar='~', quoting=csv.QUOTE_NONE)
            filewriter.writerow([repo.id, clean_data])

print 'all done!'
