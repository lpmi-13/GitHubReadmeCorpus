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
    except:
        data = ''

    string_data = str(data)

    clean_data = string_data.replace('\n', '')

    return clean_data

    
