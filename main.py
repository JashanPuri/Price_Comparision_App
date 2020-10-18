from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to our price tracking app's api"


@app.route('/api/flipkart')
def flipkart_api():
    return 'Hello  i m Nishant'


@app.route('/api/amazon', methods=['GET'])
def amazon_api():
    # print('chandu here')
    if request.method == 'GET':
        uri = 'https://www.amazon.in'
        query = str(request.args['query'])
        # print(query)
        if " " in query:
            query = str(query).replace(" ", "+")
        else:
            pass
        search = '/s?k=' + query
        finaluri = uri + search
        print(finaluri)
        src = requests.get(finaluri).content
        soup = BeautifulSoup(src, 'html.parser')
        name_list = soup.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        price_list = soup.find_all('span', {'class': 'a-price-whole'})
        l = []
        print(len(name_list))
        print(len(price_list))
        if len(name_list) > 0 and len(price_list) > 0:
            j = 0
            for i in range(len(name_list) - len(price_list), len(name_list)):
                d = {}
                d['title'] = name_list[j].text
                d['price'] = price_list[j].text
                j += 1
                l.append(d)

    return jsonify(l)


@app.route('/api/croma', methods=['GET'])
def croma_api():
    if request.method == 'GET':
        u = 'https://www.croma.com'
        text = str(request.args['text'])
        print(text)
        if " " in text:
            text = str(text).replace(" ", "%20")
        else:
            pass
        search = '/search/?text=' + text
        finalurl = u + search
        print(finalurl)
        body = requests.get(finalurl).content
        soup = BeautifulSoup(body, 'html.parser')
        print(soup.prettify())
        links = soup.find_all('a', {'class': 'product-title'})
        print(links)
        l = []
        for i in links:
            d = {}
            p_url = u + i.get('href')
            p_content = requests.get(p_url).content
            p_soup = BeautifulSoup(p_content, 'html.parser')
            d['p'] = p_soup.find('h1', {'class': 'pd-title'}).text
            d['price'] = p_soup.find('span', {'class': 'amount'}).text
            l.append(d)
    return jsonify(l)


if __name__ == '__main__':
    app.run()
