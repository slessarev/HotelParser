import pars
import requests
from bs4 import BeautifulSoup as BS
import csv





ls_url = pars.get_url_list(1)

# for item in ls_url:
#     print(pars.get_data(item))


with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    # записываем каждую строку из списка в файл
    for item in ls_url:
        data_list = pars.get_data(item)
        print(data_list)
        writer.writerow(data_list)
