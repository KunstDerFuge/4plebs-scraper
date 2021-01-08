import json
import requests


def search4plebs():

    with open('search_params.json', 'r') as params_file:
        params_string = params_file.read()
        params = json.loads(params_string)

    output = params['output_file']
    del params['output_file']

    print('Running search...')

    api_url_base = "http://archive.4plebs.org/_/api/chan/search/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

    response = requests.get(api_url_base, params=params, headers=headers)
    print('Search complete! \nWriting to {}...'.format(output))

    with open(output, 'w') as f:
        f.write(json.dumps(response.json(), indent=4))

    print('Wrote to {}!'.format(output))


search4plebs()
