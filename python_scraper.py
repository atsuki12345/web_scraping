import csv
from typing import List

import requests
import lxml.html

def main():
    '''
    Main method.
    :return: fetch(),scrape(),save()
    '''
    url = 'https://gihyo.jp/dp'
    html = fetch(url)
    books = scrape(html,url)
    save('books.csv',books)

def fetch(url):
    """
    get web page from PARAM URL
    :param url:
    :return:str HTML
    """
    r = requests.get(url)
    return r.text

def scrape(html,base_url):
    '''

    :param html:
    :param base_url:
    :return: dict of books
    '''
    books = []
    html = lxml.html.fromstring(html)
    html.make_links_absolute(base_url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content()
        books.append({'url':url,'title':title})
    return books

def save(file_path,books):
    '''
    Save csv file
    :param file_path:
    :param books:
    :return: None
    '''
    with open('file_path','w',newline='') as f:
        writer = csv.DictWriter(f,['url','title'])
        writer.writeheader()
        writer.writerows(books)

if __name__ == '__main__':
    main()