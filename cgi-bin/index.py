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
    headers ={
        'authority': 'www.amazon.co.uk',
        'method': 'GET',
        'path': '/Great-Gatsby-Wisehouse-Classics/dp/9176371212/ref=sr_1_1?dchild=1&keywords=9176371212&qid=1598943214&sr=8-1',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,bg;q=0.6,ky;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': 'session-id=262-6634786-7643843; i18n-prefs=GBP; ubid-acbuk=260-3704547-9411269; _rails-root_session=S2RGZ1J2VzVjSHpwVTRrazhpVFBBSG5kYkh4TTc5NnR1YWVQVGtCVFJ1NSthOGdOenJ1dVRXOTJSM3pYaEQ4ZlkyVmxEYVNDRkhkZDB4ZWQxQ2djNzhPY3NFSjZaZzFhTnRmajJVQ3JmeU1jR3UwMzlvWER6bjZzUjF0N29LbFlZL3lxV3lyMXdScWVxR0UrTEpuMEN4aHRsZ0JJZktLa3QySlVKOHh0VDNFZE1HZEVjZFN5alBnUTVBWWM4OFh5LS1WSWpzdTdwbW45aU4vU2hCMFJpVkFBPT0%3D--193fc10cb02a3f245ce4129404dc31cef2929334; lc-acbuk=en_GB; session-token=2dmdMBlpo9KfuZjWw116l63AKhXPMPTbKQbMYda42uVRXiiXdfqTJwWeiaRMbvnEKy4ZRgkuJp12xci6BS3MomUoSalZRj5VEWM+woNT7STkk1LCpu1fbnkHTHKBD+C88SBJejxPyCvoTrMGJVYKMM71zg706RBgOCMphRwttbYElUztJ6iBWxxmpgsqWKji; session-id-time=2082787201l; csm-hit=adb:adblk_no&t:1599036248088&tb:YT4HYR18M3FW8F74DXRG+s-YT4HYR18M3FW8F74DXRG|1599036248088',
        'downlink': '0.8',
        'ect': '4g',
        'referer': 'https://www.amazon.co.uk/s?k=9176371212&ref=nb_sb_noss',
        'rtt': '200',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

    page = c.get(url, headers=headers)

    soup = BeautifulSoup(page.content.replace("<!--[if IE 6]>", "").replace("<![endif]-->", ""), 'html.parser')

    #print(soup)

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

    print('{"title":"' + title.strip() + '",' + images.replace("'imageGalleryData' :", '"imageGalleryData" :').strip() + '}],"description":"' + description.replace("</noscript>", "").replace("<noscript>", "").replace("<em></em>", "").replace('"', "'").strip() + '"}')
