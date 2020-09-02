#!/usr/bin/python

import requests
from bs4 import BeautifulSoup



import sys, codecs, cgi

#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
findValue = form.getvalue('findValue')

print("Content-type:text/plain;charset=utf-8\r\n\r\n")
#print(findValue)
#findValue = '4345265460'

with requests.Session() as c:
    url = 'https://www.amazon.co.uk/s?k=' + findValue
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

    http_proxy  = "http://77.111.246.13"
    https_proxy = "https://77.111.246.13"
    ftp_proxy   = "ftp://77.111.246.13"

    proxyDict = {
        "http"  : http_proxy,
        "https" : https_proxy,
        "ftp"   : ftp_proxy
    }

    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
    }

    page = c.get(url, proxies=proxyDict)

    soup = BeautifulSoup(page.content.replace("<!--[if IE 6]>", "").replace("<![endif]-->", ""), 'html.parser')

    print(soup)

    href= soup.find("h2").find("a", {"class" : "a-link-normal"}).get('href')

    #print(href)

    url = 'https://www.amazon.co.uk' + href
    #print(url)
    page = c.get(url, proxies=proxyDict)
    soup = BeautifulSoup(page.content.replace("<!--[if IE 6]>", "").replace("<![endif]-->", ""), 'html.parser')

    title = soup.find("span", {"id" : "productTitle"}).get_text()
    #print(soup.find("span", {"id" : "productSubtitle"}).get_text())

    images = page.content[ page.content.find("'imageGalleryData' : [") : len(page.content) ][ 0 : page.content[ page.content.find("'imageGalleryData' : [") : len(page.content) ].find("}],")]

    description =  page.content[ page.content[ 0 : page.content.find('<div id="outer_postBodyPS"') ].rfind("<noscript>") : page.content.find('<div id="outer_postBodyPS"') ]

    print('{"title":"' + title.strip() + '",' + images.replace("'imageGalleryData' :", '"imageGalleryData" :').strip() + '}],"description":"' + description.replace("</noscript>", "").replace("<noscript>", "").replace("<em></em>", "").replace('"', "'").strip() + '"}')
