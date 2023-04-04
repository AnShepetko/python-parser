
import requests;
from bs4 import BeautifulSoup;


def requests_func_descriptions(max_page, path):
    descriptions_text_list = []
    for page in range(max_page):
        page_info = requests.get(f'{path}page={page}')
        page_info_soup = BeautifulSoup(page_info.text, 'html.parser')
        vacancy_container = page_info_soup.find_all('div', {'class': 'card card-hover card-visited wordwrap job-link'})

        for description in vacancy_container:
            descriptions_text_list.append(description.find('p', {'class': 'overflow text-muted add-top-sm cut-bottom'}).text)
            
    return descriptions_text_list
