from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to our price tracking app's api"


@app.route('/api/flipkart')
def flipkart_api():
    if request.method == 'GET':
        u = 'https://www.flipkart.com'
        text = str(request.args['query'])
        print(text)
        if " " in text:
            text = str(text).replace(" ", "%20")
        else:
            pass
        search = '/search?q=' + text
        finalurl = u + search
        print(finalurl)
        body = requests.get(finalurl).content
        soup = BeautifulSoup(body, 'html.parser')
        # print(soup.prettify())
        links = soup.find_all('a', {'class': '_31qSD5'})
        print(links)
        l = []
        for i in links:
            d = {}
            p_url = u + i.get('href')
            p_content = requests.get(p_url).content
            p_soup = BeautifulSoup(p_content, 'html.parser')
            d['title'] = p_soup.find('span', {'class': '_35KyD6'}).text
            d['price'] = p_soup.find('div', {'class': '_1vC4OE _3qQ9m1'}).text
            d['link'] = p_url
            l.append(d)
    return jsonify({'flipkart': l})


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
        n = []
        for i in name_list:
            n.append(i.text)
        print(n)
        if len(name_list) > 0 and len(price_list) > 0:
            for i in range(min((len(name_list), len(price_list)))):
                d = dict()
                d['title'] = name_list[i].text
                d['price'] = price_list[i].text
                l.append(d)

    return jsonify({'amazon': l})


@app.route('/api/reliance', methods=['GET'])
def reliance_api():
    #print('my contribution :)')
    if request.method == 'GET':
        u = 'https://www.reliancedigital.in'
        #converting the request in query to string and storing it
        text = str(request.args['query'])
        print(text)
        if " " in text:
            text = str(text).replace(" ", "%20")
        else:
            pass
        search = '/search/?q=' + text + ':relevance'
        finalurl = u + search
        print(finalurl)
        body = requests.get(finalurl).content                  #getting source code in unicode format
        soup = BeautifulSoup(body, 'html.parser')              #parsing the source code
        #print(soup.prettify())
        div_tags = soup.find_all('div', {'class': 'sp grid'})  #finding akl div tags
        print(div_tags)
        l = []
        for i in div_tags:
            d = {}
            sib_soup = BeautifulSoup(str(i), 'html.parser')    #parsing all data within div tag having class : sp grid
            p_url = u + sib_soup.a['href']                     #finding and adding all the links to the products into the original link
            p_content = requests.get(p_url).content            #getting source code of the product page
            p_soup = BeautifulSoup(p_content, 'html.parser')
            d['title'] = p_soup.find('div', {'class': 'pdp__title'}).text
            d['price'] = p_soup.find('span', {'class': 'pdp__offerPrice'}).text
            # d['price'] = d['price'].replace("\u20b9", "")
            d['link'] = p_url

            l.append(d)
    return jsonify({'reliance': l})


if __name__ == '__main__':
    app.run()
