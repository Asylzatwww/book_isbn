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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    page = c.get(url, headers=headers)

    soup = BeautifulSoup(page.content.replace("<!--[if IE 6]>", "").replace("<![endif]-->", ""), 'html.parser')

    href= soup.find("h2").find("a", {"class" : "a-link-normal"}).get('href')

    #print(href)

    url = 'https://www.amazon.co.uk' + href
    #print(url)
    page = c.get(url, headers=headers)
    soup = BeautifulSoup(page.content.replace("<!--[if IE 6]>", "").replace("<![endif]-->", ""), 'html.parser')

    title = soup.find("span", {"id" : "productTitle"}).get_text()
    #print(soup.find("span", {"id" : "productSubtitle"}).get_text())

    images = page.content[ page.content.find("'imageGalleryData' : [") : len(page.content) ][ 0 : page.content[ page.content.find("'imageGalleryData' : [") : len(page.content) ].find("}],")]

    description =  page.content[ page.content[ 0 : page.content.find('<div id="outer_postBodyPS"') ].rfind("<noscript>") : page.content.find('<div id="outer_postBodyPS"') ]

    print('{"title":"' + title + '",' + images + '}],"description":"' + description.replace("</noscript>", "") + '"')
