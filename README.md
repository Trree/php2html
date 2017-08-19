# php2html
Convert PHP pages to HTML pages

## ENV

- python
- [scrapy](https://docs.scrapy.org/en/latest/)

## WHY
  - fast
  - safe


## HOW

```
scrapy crawl php
python filesed.py
```

## FILE 

**You should change following file according to your needs**

  - php2html/spiders/php.py 
    - spiders file 

  - filesed.py 
    - replace php to html in the files.

## ISSUES

- Place the file in the appropriate directory according to the url path
