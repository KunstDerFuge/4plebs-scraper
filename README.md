# 4plebs-scraper
Search and archive posts from the 4plebs API

Only prerequisite is `requests`:

```
pip install requests
```

### Search mode
Edit `search_params.json` and run `python search.py`. Output will be written to the file you specify, and overwritten every time.

### Thread archive mode
Keep notes of threads you'd like to archive in `threads.txt`. An example file is given. Write the board name you'd like to scrape, and the threads on individual lines below that. running `python threads.py` will check the archive, and if a thread hasn't already been scraped, it will do so.

See the [4plebs API documentation](https://4plebs.tech/foolfuuka/#basic-foolfuuka-properties) for more info on the parameters of the /search/ endpoint


Based on some code from the script at https://github.com/JakapunTachaiya/4plebs_rest
