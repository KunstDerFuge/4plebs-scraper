import json
import requests

api_url_base = "http://archive.4plebs.org/_/api/chan/thread/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

archive = {}

try:
    with open('archive.json', 'r') as archive_file:
        archive = json.loads(archive_file.read())
        
    archive_file.close()

except Exception as e:
    print('\nCould not load archive:')
    print(e)
    exit(1)

try:
    with open('threads.txt', 'r') as threads_file:
        threads_list = threads_file.readlines()

    board = ''

    for line in threads_list:
        try:
            cleaned = line.strip()
            if cleaned == '':
                # Blank line
                continue

            if cleaned.isnumeric():
                # Thread num
                thread = int(cleaned)
                if board in archive and str(thread) in archive[board]:
                    print('/{}/{} already archived. Continuing...'.format(board, thread))
                else:
                    # Scrape it
                    print('Scraping /{}/{}...'.format(board, thread))
                    response = requests.get(api_url_base, params={'board': board, 'num': thread}, headers=headers)

                    if board not in archive:
                        archive[board] = {}

                    archive[board][thread] = response.json()[str(thread)]
            else:
                # Board
                board = cleaned.replace(':', '')
        except Exception as e:
            print('Exception while scraping:')
            print(e)

    # Write archive
    
    with open('archive.json', 'w') as archive_file:
        archive_file.write(json.dumps(archive, indent=4))

    print('Done!')

except Exception as e:
    print('Exception while trying to scrape threads!')
    print(e)
