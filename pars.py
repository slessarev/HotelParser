import requests
from bs4 import BeautifulSoup as BS
import csv
import sendmail
import time
import datetime


# def fed_number(page):
#     # функция принимает на вход номер страницы и возвращает список из 10 номеров поля Порядковый номер в Федеральном перечне.

#     # Читаем данные по адресу
#     r = requests.get("https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai/displayAccommodation/index?Accommodation%5BFullName%5D=&Accommodation%5BRegion%5D=%D0%A0%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0+%D0%9A%D1%80%D1%8B%D0%BC&Accommodation%5BKey%5D=&Accommodation%5BOrganizationId%5D=&Accommodation%5BCertificateNumber%5D=&Accommodation%5BInn%5D=&Accommodation%5BOgrn%5D=&Accommodation%5BSolutionNumber%5D=&yt0=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&Accommodation_page=" + str(page))
#     html = BS(r.content, 'lxml')
#     numbers = html.find_all("div", class_="field object-region")

#     # преобразоваваем данные в список
#     result = list()
#     count_number = str()
#     for item in numbers:
#         result.append(item.text)

#     # В строку записываем только номера через пробелл
#     for item in result:
#         for j in range(len(item)):
#             if item[j].isdigit():
#                 count_number = count_number + str(item[j])
#         count_number = count_number + ' '

#     # преобразовали строку в список через разделитель - пробел
#     count_number = list(map(int, count_number.split()))
#     # print(count_number)
#     return count_number


def get_data(link, retry=5):
    # Функция возвращает значения ИНН, телефон, почта изкарточки организации
    try: 
        r = requests.get("https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai" + str(link))
    except Exception as ex:
        time.sleep(1)
        if retry:
            print(f"[INFO] retry={retry} => {link}")
            return get_data(link, retry=(retry-1))
        else: raise
    else:
        html = BS(r.content, 'lxml')
        inn = html.find("div").find_all("span")
        data_str = list()
        data_str.append(inn[2].text)
        data_str.append(inn[14].text)
        data_str.append(inn[0].text)
        data_str.append(inn[20].text)
        data_str.append(inn[23].text)
        return data_str


def get_url_list(page, retry=5):
    # функция, которая возвращает ссылки на страницы отелей
    try: 
        r = requests.get("https://xn----7sba3acabbldhv3chawrl5bzn.xn--p1ai/displayAccommodation/index?Accommodation%5BFullName%5D=&Accommodation%5BRegion%5D=%D0%A0%D0%B5%D1%81%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0+%D0%9A%D1%80%D1%8B%D0%BC&Accommodation%5BKey%5D=&Accommodation%5BOrganizationId%5D=&Accommodation%5BCertificateNumber%5D=&Accommodation%5BInn%5D=&Accommodation%5BOgrn%5D=&Accommodation%5BSolutionNumber%5D=&yt0=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&Accommodation_page=" + str(page))
    except Exception as ex:
        time.sleep(1)
        if retry:
            print(f"[INFO] retry={retry} => {page}")
            return get_url_list(page, retry=(retry-1))
        else: raise
    else:
        html = BS(r.content, 'lxml')
        link = html.find_all("a", class_="object-title")
        # print(link)
        item_url = list()
        for item in link:
            item_url.append(item.get("href"))
        return item_url


def csv_writer(ls_url):
    with open('data.csv', 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        for item in ls_url:
            try:
                rec_element = get_data(item)
            except Exception as ex:
                continue
            else:
                if rec_element[0] in open('data.csv', encoding="utf-8").read():
                    print(f"{datetime.datetime.now()} || Status -> Skip")
                else:
                    print(f"{datetime.datetime.now()} || Status -> Writed")
                    writer.writerow(rec_element)
                    sendmail.send_email("Появилась новая запись: \n" + str(rec_element))
                    sendmail.send_email("Появилась новая запись: \n" + str(rec_element))
                print(rec_element)
            
def parser():
    i=1
    breake_flag = list()
    while True:
        try:
            ls_url = get_url_list(i)
        except Exception as ex:
            continue
        if breake_flag != ls_url:
            csv_writer(ls_url)
            breake_flag=ls_url
            i+=1
        else:
            break