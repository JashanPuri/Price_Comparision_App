from flask import Flask

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


@app.route('/api/croma')
def croma_api():
    print("Mujhe last kyu rakha :(")
    return 'Hello Charles'


if __name__ == '__main__':
    app.run()
