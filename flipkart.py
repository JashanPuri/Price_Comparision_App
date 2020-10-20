from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

def FlipkartProducts(text):
    u = 'https://www.flipkart.com'
    # converting the request in query to string and storing it.
    print(text)
    if " " in text:
        text = str(text).replace(" ", "%20")
    else:
        pass
    search = '/search?q=' + text
    finalurl = u + search
    print(finalurl)
    body = requests.get(finalurl).content  # getting source code in unicode format.
    soup = BeautifulSoup(body, 'html.parser')  # parsing the source code.
    # print(soup.prettify())
    links = soup.find_all('a', {'class': '_31qSD5'})
    # print(links)
    l = []
    for i in links:
        d = {}
        p_url = u + i.get('href')  # finding and adding all the links to the products into the original link.
        p_content = requests.get(p_url).content  # getting source code of the product page.
        p_soup = BeautifulSoup(p_content, 'html.parser')  # parsing all data within div tag having class : sp grid.
        d['title'] = p_soup.find('span', {'class': '_35KyD6'}).text
        d['price'] = p_soup.find('div', {'class': '_1vC4OE _3qQ9m1'}).text

        d['link'] = p_url
        l.append(d)
    print(l)
    return jsonify({'flipkart': l})

