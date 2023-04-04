import requests;
from bs4 import BeautifulSoup;

def requests_href_page(max_page, path):

    links_src = []
    for page in range(max_page):
        page_info = requests.get(f'{path}page={page}')
        page_info_soup = BeautifulSoup(page_info.text, 'html.parser')
        links = page_info_soup.find_all('h2')
        for link in links:
            text_of_link = link.find('a')['href']
            text_of_link = text_of_link[1:]
            links_src.append(text_of_link)

    return links_src
    