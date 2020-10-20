from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import flipkart as f
import amazon as a
import reliance as r

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to our price tracking app's api"


@app.route('/api/flipkart')
def flipkart_api():
    # print("i m nishant").
    if request.method == 'GET':
        text = str(request.args['query'])
        return f.FlipkartProducts(text)



@app.route('/api/amazon', methods=['GET'])
def amazon_api():
    # print('chandrima here')
    if request.method == 'GET':
        # converting the request in query (item being searched for) to string and storing it
        query = str(request.args['query'])
        # print(query)
        return a.AmazonProducts(query)


@app.route('/api/reliance', methods=['GET'])
def reliance_api():
    # print('my contribution :)')
    if request.method == 'GET':
        # converting the request in query to string and storing it
        text = str(request.args['query'])
        print(text)
        return r.RelianceProducts(text)


if __name__ == '__main__':
    app.run()
