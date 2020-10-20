from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

def RelianceProducts(text):
    u = 'https://www.reliancedigital.in'
    if " " in text:
        text = str(text).replace(" ", "%20")
    else:
        pass
    search = '/search/?q=' + text + ':relevance'
    finalurl = u + search
    print(finalurl)
    body = requests.get(finalurl).content  # getting source code in unicode format
    soup = BeautifulSoup(body, 'html.parser')  # parsing the source code
    # print(soup.prettify())
    div_tags = soup.find_all('div', {'class': 'sp grid'})  # finding all div tags
    print(div_tags)
    l = []
    count = 0
    for i in div_tags:
        d = {}
        if count == 6:
            break
        count += 1
        sib_soup = BeautifulSoup(str(i), 'html.parser')  # parsing all data within div tag having class : sp grid
        p_url = u + sib_soup.a['href']                   # finding and adding all the links to the products into the original link
        p_content = requests.get(p_url).content          # getting source code of the product page
        p_soup = BeautifulSoup(p_content, 'html.parser')
        d['title'] = p_soup.find('div', {'class': 'pdp__title'}).text
        d['price'] = p_soup.find('span', {'class': 'pdp__offerPrice'}).text
        d['link'] = p_url

        l.append(d)
    return jsonify({'reliance': l})
