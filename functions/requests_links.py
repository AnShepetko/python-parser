
import requests;
from bs4 import BeautifulSoup;


def requests_func_links(max_page, path):
    links = []
 
    for page in range(max_page):

        page_info = requests.get(f'{path}page={page}') # response from server
        page_info_soup = BeautifulSoup(page_info.text, 'html.parser') # HTML text

        vacancy = page_info_soup.find_all('div',{'class':'card card-hover card-visited wordwrap job-link'}) # container of vacancy
        for a in vacancy:  # search links in container and adding them in list  (27 str)
           links.append(a.find('a').text)
    return links 