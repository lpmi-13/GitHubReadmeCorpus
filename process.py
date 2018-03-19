import re

def process_id(name):
    result = re.findall(r'\d+', name)
    try:
        return int(result[0])
    except IndexError:
        return 0

def extract_string_content(repo):
    try:
        readme = repo.get_readme() or ''
        data = readme.decoded_content
        string_data = str(data, 'utf-8')
        string_data = string_data.replace('\n','')
    except:
        string_data = ''


    return string_data
