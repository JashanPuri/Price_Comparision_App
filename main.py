from flask import Flask,request,jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to our price tracking app's api"


@app.route('/api/flipkart')
def flipkart_api():
    return 'Hello  i m Nishant'


@app.route('/api/amazon')
def amazon_api():
    print("thanks for not putting me last :)")
    return 'Hello Chandrima'


@app.route('/api/croma',methods=['GET'])
def croma_api():
    if request.method == 'GET':
        u = 'https://www.croma.com/'
        text = str(request.args['text'])
        print(text)
        if " " in text:
            text = str(text).replace(" ", "%20")
        else:
            pass
        search = '/search_results?q=' + text
        finalurl = u + search
        print(finalurl)
        body = requests.get(finalurl).content
        scrap = BeautifulSoup(body, 'html.parser')
        links = scrap.find_all('a', {'class': 'product-title'})
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
