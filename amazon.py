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
        src = requests.get(finaluri).content                 # getting search result page source code in unicode format
        soup = BeautifulSoup(src, 'html.parser')             # using beautiful soup to parse source code
        name_list = soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        price_list = soup.find_all('span', {'class': 'a-price-whole'})
        link_list = soup.find_all('a', {'class': 'a-link-normal a-text-normal'})
        l = []
        print(len(name_list))
        print(len(price_list))
        print(len(link_list))
        n = []
        for i in name_list:                                          # printing names of items on search page
            n.append(i.text)
        print(n)
        if len(name_list) > 0 and len(price_list) > 0:               # checking if no of search results > 0
            # adding all items with name,price, link to dictionary
            count = 0
            for i in range(min((len(name_list), len(price_list), len(link_list)))):
                if count == 6:
                    break
                count += 1
                d = dict()
                d['title'] = name_list[i].text
                d['price'] = price_list[i].text
                d['link'] = uri + link_list[i].get('href')          # adding url of amazon to item link
                l.append(d)

        return jsonify({'amazon': l})                                   # return list l in JavaScript Object Notation
