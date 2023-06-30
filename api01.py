import requests

user_agent = {'User-agent': 'Mozilla/5.0'}
url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/KO?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
r = requests.get(url, headers=user_agent)
print (r.json())