import pars
import requests
from bs4 import BeautifulSoup as BS





ls_url = pars.get_url_list(1)

for item in ls_url:
    print(pars.get_data(item))
