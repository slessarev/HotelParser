import pars
from bs4 import BeautifulSoup as BS
import schedule



def main():
    schedule.every().hour.do(pars.parser)
    while True:
        schedule.run_pending()
        pars.parser()


if __name__ == '__main__':
    main()

# Добавить: 
# обработку ошибок
# запуск каждый час в рабочее время / почти готово
# логирование
# асинхронность