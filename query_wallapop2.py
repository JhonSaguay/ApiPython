import urllib.parse
import requests

def get_wallapop(search_text: str):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    keywords = search_text
    keywords = urllib.parse.quote(keywords)
    url = f"https://api.wallapop.com/api/v3/cars/search?category_ids=100&keywords={keywords}&filters_source=suggester&longitude=-3.69196&latitude=40.41956"

    r = requests.get(url, headers=user_agent)

    print(r.json())
    search_results = r.json()['search_objects']
    price_sum = 0
    num_elements = len(search_results)
    
    if num_elements == 0: {
        "num_results": num_elements,
        "price_avg": None,
        "results": [],
    }

    results = []
    for r in search_results:
        articulo = {
            "price": r["content"]["price"],
            "title": r["content"]["title"],
            "storytelling": r["content"]["storytelling"]
        }

        results.append(articulo)
        print("-------------------------------------")
        
        price_sum = price_sum + r["content"]["price"]

    price_avg = price_sum / num_elements
    
    return {
        "num_results": num_elements,
        "price_avg": price_avg,
        "results": results,
    }