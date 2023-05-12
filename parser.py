import pars
from bs4 import BeautifulSoup as BS
import schedule



def main():
    schedule.every().hour.do(pars.parser)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    print('Starting. Wait 1h befor parsing...')
    main()

# Добавить: 
# DONE обработку ошибок
# DONE запуск каждый час в рабочее время / почти готово
# логирование
# асинхронность