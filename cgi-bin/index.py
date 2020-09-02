#!/usr/bin/python

import requests
from bs4 import BeautifulSoup



import sys, codecs, cgi

#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
findValue = form.getvalue('findValue')
#http://biznen.com/cgi-bin/index.py?findValue=4345265460

print("Content-type:text/plain;charset=utf-8\r\n\r\n")
print(findValue)
#findValue = '4345265460'

with requests.Session() as c:
    #url = 'http://www.k-agent.ru/search-of-companies'
    url = 'https://www.amazon.co.uk/s?k=' + findValue
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    #r = requests.get(url, headers=headers)
    page = c.get(url, headers=headers)
    #login_data = dict(tbFindValue=findValue, __EVENTTARGET='lbFindTop', next='/')
    #print(page.content)
    #page = c.post(url, data=login_data, headers={"Referer": url})

    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    #r = requests.get(url, headers=headers)

    #print(page.content)

    soup = BeautifulSoup(page, 'html.parser')

    print(soup)

    href= soup.find("h2")#.get('href')

    print(href)

    dd = soup.find("div")
    print(dd)
    print(soup.title.string)

    print("ss")
    url = 'http://www.k-agent.ru' + href
    print(url)
    page = c.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.title.string)
    #href = soup.find("table", attrs={"class": "compdate"}).find_all("td")
    json = '{'
    i = 0
    for node in soup.find("table", attrs={"class": "compdate"}).find_all("td"):
        i += 1
        json += '"field' + str(i) + '" : "' + str(node.findAll(text=True)).replace('"', '').replace("'", "").replace("[", "").replace("]", "") + '", '
    #print(page.content)
    json = json[:-2]
    json += '}'
    print(json)
    #print(href)