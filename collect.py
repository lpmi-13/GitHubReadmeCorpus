import os
from github import Github
import requests, base64, yaml
from pymongo import MongoClient

g = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'], timeout=200, per_page=30)

'''
this call is the same as hitting the GitHub search API endpoint:
https://api.github.com/repositories, which yields every
publicly available repository on GitHub
'''

db = MongoClient().github

highest_repo = list(db.repo.find().sort('repoId',-1).limit(1))

highest_id = highest_repo[0]['repoID']


if highest_id != None and highest_id_> 0:
    skip_id = highest_id
else:
    skip_id = 0

results = g.get_repos(since=skip_id)

write_text = open('readmeText.txt', 'w')
#write_text.truncate()

write_urls = open('urls.txt', 'w')
#write_urls.truncate()

for repo in results:
    result = db.repo.find({'repoID': repo.id})
    if result.count() > 0:
        pass
    else:

        print ('processing {}').format(repo.id)
        result = db.repo.insert_one({
            "repoID" : repo.id
        })

	print (result)

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
