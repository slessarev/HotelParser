import pars
import requests
from bs4 import BeautifulSoup as BS

i=1
breake_flag = list()
while True:
    
    ls_url = pars.get_url_list(i)
    if breake_flag != ls_url:
        pars.csv_writer(ls_url)
        breake_flag=ls_url
        i+=1
    else:
        break
