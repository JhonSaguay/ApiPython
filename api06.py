from flask import Flask, request
from query02 import get_company_information
from query_wallapop2 import get_wallapop

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello WorLd!"

@app.route('/api/yahoo')
def get_company():
    symbol = "DIS"
    return get_company_information(symbol)

@app.route('/api/wallapop')
def get_product_and_price_average():
    query = request.args.get("search_text")
    if query is None:
        return{}
    return get_wallapop(query)

if __name__ == '__main__':
    app.run()