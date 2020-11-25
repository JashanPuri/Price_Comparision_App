from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

def AmazonProducts(query):
    if " " in query:
        query = str(query).replace(" ", "+")
    else:
        pass
    uri = 'https://www.amazon.in'
    search = '/s?k=' + query
    finaluri = uri + search
    print(finaluri)
    headers = {
        'Host': 'www.amazon.in',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers'

    }
    src = requests.get(finaluri,headers=headers).content  # getting search result page source code in unicode format
    soup = BeautifulSoup(src, 'html.parser')  # using beautiful soup to parse source code
    name_list = soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    price_list = soup.find_all('span', {'class': 'a-price-whole'})
    link_list = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})
    image_list = soup.find_all('img', {'class': 's-image'})
    l = []
    # print(image_list)
    print(len(name_list))
    print(len(price_list))
    print(len(link_list))
    print(len(image_list))
    n = []
    for i in range(10):
        if 'm.media-amazon' not in image_list[i].get('src'):
            image_list.remove(image_list[i])
    for i in name_list:  # printing names of items on search page
        n.append(i.text)
    print(n)
    if len(name_list) > 0 and len(price_list) > 0:  # checking if no of search results > 0
        # adding all items with name,price, link to dictionary
        count = 0
        for i in range(min((len(name_list), len(price_list), len(link_list)))):
            if count == 6:
                break
            count = count + 1
            d = dict()
            d['title'] = name_list[i].text
            d['price'] = price_list[i].text
            d['link'] = uri + link_list[i].get('href')  # adding url of amazon to item link
            d['imgUrl'] = image_list[i].get('src')
            l.append(d)

    return jsonify({'amazon': l})  # return list l in JavaScript Object Notation
