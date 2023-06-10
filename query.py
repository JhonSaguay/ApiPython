import requests
url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/INTC?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
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
    print(my_data_selection)