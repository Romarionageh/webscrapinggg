import requests
from bs4 import BeautifulSoup
def get_title(soup):
        title = soup.find("span", attrs={"id": 'productTitle'})
        name=title.text
        return name

def get_price(soup):
    try:
        price = soup.find("span", attrs={"class": "a-price-whole"})
        total = price.text
    except AttributeError:
        total=""
    return total
HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
page_num=1
while True:
    if (page_num>7):
        print("page ended")
        break
    URL =f"https://www.amazon.eg/s?k=samsung+mobile+phone&page={page_num}&language=ar_AE&crid=1T8VYYD0M0RIS&qid=1671313412&sprefix=samsung+mo%2Caps%2C2821&ref=sr_pg_{page_num}"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    links_list = []
    for link in links:
        links_list.append(link.get('href'))
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.eg"+link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        print("Product Title =", get_title(new_soup))
        print("Product Price =", get_price(new_soup))
        print()
    page_num += 1
    print("switched")
