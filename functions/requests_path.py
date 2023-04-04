
import requests;
from bs4 import BeautifulSoup;

path = 'https://www.work.ua/jobs-python/'
def page_handler():
   
    work = requests.get(path)
    work_soup = BeautifulSoup(work.text, 'html.parser')



    links = work_soup.find('ul' , {'class':'pagination hidden-xs'}).find_all('a')
    links.pop()

    list_pages = []

    for link in links:
        list_pages.append(int(link.text))


    return list_pages[-1]

