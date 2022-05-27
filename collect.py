from github import Github
import requests
import csv
import os
from datetime import datetime
from rateLimit import return_rate_limit
from process import process_id, extract_string_content


SAVE_DIRECTORY = 'data/'
highest_repo_id = 0

# we set this here so we can stop the script and restart it without needing
# to collect from the beginning again
for fn in os.listdir(SAVE_DIRECTORY):
    if int(process_id(fn)) > highest_repo_id:
        highest_repo_id = int(process_id(fn))


g = Github(os.environ['GITHUB_TOKEN'], timeout=200, per_page=30)

'''
this call is the same as hitting the GitHub search API endpoint:
https://api.github.com/repositories, which yields every
publicly available repository on GitHub
'''

print('highest repo id is ' + str(highest_repo_id))

results = g.get_repos(since=highest_repo_id)


for repo in results:
    print ('processing {}'.format(repo.id))

    #check rate limit
    rate = return_rate_limit(g)
    print(f'remaining API calls this hour: {rate}')
    print(f'{str(datetime.now())}')

    if(rate > 250 and not repo.fork):

        response = requests.get(repo.html_url)
        '''
        this check is just to make sure that the repo still
        exists. It might not be needed, though omitting this
        check has caused issues in past projects using the GitHub
        API, so leaving it in for now
        '''
        if response.headers.get('status') is not int(404):
            print(f'processing README for {repo.html_url}...')

            readme_data = extract_string_content(repo)

            #writes the readme text, if it exists, to a csv file
            filename = f'repo-{repo.id}.csv'
            path_to_file = SAVE_DIRECTORY + filename

            with open(path_to_file, 'wt') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', escapechar='~', quoting=csv.QUOTE_NONE)
                filewriter.writerow([repo.id, readme_data])

# very ambitious...we'll probably never get here
print('all done!')
