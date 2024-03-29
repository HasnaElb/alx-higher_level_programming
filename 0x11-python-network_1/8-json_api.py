#!/usr/bin/python3
"""0x11. Python - Network #1, task 8. Search API
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    response = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = response.json()
    except ValueError:
        if response.status_code == 204:
            print('No result')
        else:
            print('Not a valid JSON')
    else:
        if not json_dict:
            print('No result')
        else:
            print('[{}] {}'.format(json_dict.get('id'), json_dict.get('name')))
