from functions.requests_path import page_handler #requests_func_links, requests_func_descriptions;
from functions.requests_href_page import requests_href_page;
from functions.requests_links import requests_func_links
from functions.requests_descriptions import requests_func_descriptions;

path = 'https://www.work.ua/jobs-python/'
work_path = 'https://www.work.ua/'

max_page = page_handler()


links_vacancy = requests_func_links(max_page, path)  # links
text_of_vacancies = requests_func_descriptions(max_page, path) # descriptions  
list_href = requests_href_page(max_page, path)


list_of_vacancy_objects = []

for vacancy in range(len(links_vacancy)):
    list_of_vacancy_objects.append(
        {
            'title': links_vacancy[vacancy],
            'href': work_path + list_href[vacancy],
            'description': text_of_vacancies[vacancy]
        }
    )
print(list_of_vacancy_objects)