import re

def process_id(name):
    result = re.findall(r'\d+', name)
    try:
        return int(result[0])
    except IndexError:
        return 0
