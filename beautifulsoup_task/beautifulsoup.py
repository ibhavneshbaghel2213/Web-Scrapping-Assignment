from bs4 import BeautifulSoup as bs
import requests
import json

def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    #     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    with requests.get(url, headers=headers, stream=True) as res:
        soup = bs(res.text, 'html.parser')
    return soup

def get_data(url="https://webscraper.io/test-sites/e-commerce/static/computers/tablets") :
    listOfElements=[]
    for page in range(1,5) :
        urls =  url + f"?page={page}"
        soup = get_soup(urls)
        cards = soup.find_all("div", {"class": "card thumbnail"})
        for ele in cards :
            dic = {}
            name = ele.find("a",{"class":"title"}).text
            price = ele.find("h4",{"class":"price float-end card-title pull-right"}).text
            review = ele.find("div",{"class":"ratings"}).find_all('span')
            dic['name'] = name
            dic['price'] = price
            dic['review'] = len(review)
            listOfElements.append(dic)
    return listOfElements

def to_json(data):
    import json
    with open("extracted.json", "w") as outfile:
        json.dump(data, outfile, indent=4)
        outfile.close()

if __name__ == "__main__":
    data_list = get_data()
    # print(data_list)
    to_json(get_data())
