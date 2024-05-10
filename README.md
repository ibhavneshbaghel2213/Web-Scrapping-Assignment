## For Extarcting data from beautifulsoup just execute 
```
python3 beautifulsoup_task/beautifulsoup.py
```

- note: u need to install below library
   - [beautifulsoup](https://pypi.org/project/beautifulsoup4/)
   - [requests](https://pypi.org/project/requests/)




## For Extracting data using Scrapy with docker just execute
```
cd scrappy_task/testWebsite
docker build -t scrapy_project .
docker run -v .:/app scrapy_project
```
### u will see output.json in your current folder

# ------------------------------------------------------------
###  For Extracting data using scrapy without docker just execute

```
cd scrappy_task/testWebsite/testWebsite
```
```
scrapy crawl testSite
```
```
scrapy crawl testSite -o output.json
```