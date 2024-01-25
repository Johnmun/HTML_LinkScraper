import requests
from bs4 import BeautifulSoup

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        print(urls)


url = input("Enter the URL you want to scrape. ")
keyword = input("Enter the keyword to search for in the URL provided. ")
spider_urls(url, keyword)
