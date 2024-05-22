import requests
from bs4 import BeautifulSoup 
import csv


def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    #     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    with requests.get(url, headers=headers, stream=True) as res:
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
    return soup



def scrape_page(url):
    try :
        soup = get_soup(url=url)
        description = ''
        ImageUrl=''
        product_name = soup.find('h1', {'class': '_6EBuvT'}).text.replace('\u00a0','').strip()
        price = soup.find('div', {'class': 'Nx9bqj CxhGGd'}).text.replace('\u20b9','INR ').strip()
        description = soup.find('div',{'class' : "_4gvKMe"}).text.strip()
        ImageUrl = soup.find('img',{'class':"DByuf4 IZexXJ jLEJ7H"})['src']

        return {
            'product_name': product_name,
            'price': price,
            'description' : description,
            'imageUrl' : ImageUrl
        }
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except AttributeError:
        print("Some data might be missing")
        return None
    




def scrape_multiple_pages(url_list):
    products = []
    
    for i in url_list:
        product_data = scrape_page(i)
        # print(product_data)
        products.append(product_data)

    return products

def to_json(data):
    import json
    with open("flipkart_samsung.json", "w") as outfile:
        json.dump(data, outfile, indent=4)
        outfile.close()


baseUrl = "https://www.flipkart.com"

url_list = []

x=1
while x > 0 : 
    try :
        page_soup=get_soup(f"https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=178819&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.type%255B%255D%3DSmartphones&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNhbXN1bmcgc21hcnRwaG9uZXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=14.productCard.PMU_V2_13&page={x}")
        for i in page_soup.find_all('a',class_="CGtC98") :
            full_url = baseUrl + i['href']
            # print("full --->  ",full_url)
            url_list.append(full_url)
        # next_page = baseUrl + page_soup.find('a',class_="_9QVEpD")['href']
        # print("====================================================")

        # page_soup = get_soup(next_page)
        x+=1
    except Exception as e :
        # print(f"Error : {e}")
        break

products_data = scrape_multiple_pages(url_list)
to_json(products_data)





