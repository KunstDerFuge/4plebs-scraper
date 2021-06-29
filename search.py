import json
import requests
import time


def search4plebs():

    api_url_base = "http://archive.4plebs.org/_/api/chan/search/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    
    def run_search(params, headers):
        response = requests.get(api_url_base, params=params, headers=headers)
        return response.json()

    with open('search_params.json', 'r') as params_file:
        params_string = params_file.read()
        params = json.loads(params_string)

    output = params['output_file']
    del params['output_file']

    print('Running search...')

    page = 1
    posts = None

    while True:

        try:
            print('Fetching results for page {}...'.format(page))
            params['page'] = page
            results = run_search(params, headers)
            if 'error' in results:
                break
            if not posts:
                posts = results
            else:
                posts['0']['posts'].extend(results['0']['posts'])
            page += 1
            print('Waiting 12 seconds to comply with rate limiting...')
            time.sleep(12)

        except KeyboardInterrupt:
            print('Cancelled, gathering results...')
            break
    
    print('Search complete! \nWriting to {}...'.format(output))

    with open(output, 'w') as f:
        f.write(json.dumps(posts, indent=4))

    print('Wrote to {}!'.format(output))


search4plebs()
