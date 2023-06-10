import requests
from flask import Flask

app = Flask(__name__)

@app.route('/company')
def get_company():
    symbol = "DIS"
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    headers = {
        'Content-Type': 'text/html',
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url,headers = headers)
    if response.status_code ==200:
        result = response.json()['quoteSummary']['result']
        data=result[0]
        # for data in result:
        shortname= data['price']['shortName']
        symbol = data['price']['symbol']
        precio = data['summaryDetail']['previousClose']['raw']
        my_data_selection ={
            'nombre':shortname,
            'ticker':symbol,
            'precio':precio
        }
        return my_data_selection
    return 404

@app.route('/')
def hello_world():
  return "Hello world!" #if you want to render a .html file, 
                        # import render_template from flask and use 
                        #render_template("index.html") here.

if __name__ == '__main__':
    app.run()