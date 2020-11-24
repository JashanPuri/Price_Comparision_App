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
    links = soup.find_all('a', {'class': '_1fQZEK'})
    # print(links)
    l = []
    count = 0
    for i in links:
        d = {}
        if count == 6:
            break
        count += 1
        p_url = u + i.get('href')
        p_content = requests.get(p_url).content  # getting source code of the product page.
        p_soup = BeautifulSoup(p_content, 'html.parser')
        d['title'] = p_soup.find('span', {'class': 'B_NuCI'}).text
        d['price'] = p_soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text
        d['link'] = p_url
        l.append(d)
    print(l)
    return jsonify({'flipkart': l})

