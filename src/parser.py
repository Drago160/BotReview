from bs4 import BeautifulSoup as BS
import requests
from googlesearch import search
import src.Toolfunc as Toolfunc 
from src.dbParams import RequestData

class Parser:
    """Класс Парсер"""

    def __init__(self):
    """Конструктор не принимает параметров"""
        pass

    def find_all_blocks(self, url):
        """Ищет все теги div в которых содержаться ответы пользовательские на сайте"""
        page = requests.get(url)
        soup = BS(page.text, "html.parser")
        divs = soup.find_all("div", attrs= {"itemprop":"text"})
        return divs


    def find_answers(self, Error_name, reqData):
        """Обрабатывает запрос о поиске и по нему ищет необходимое кол-во запросов-ответов"""
        ip = Error_name + " stacoverflow"
        # Перебираем url'ы
        for url in search(ip, stop=reqData.questNum):
            # Если в названии есть наш сайт
            if url.find("stackoverflow"): 
                # Находим все интересные нам блоки
                divs = self.find_all_blocks(url)
                answers = []# тут все наши ответы
                counter = 0
                #Перебираем всех его детей
                
                for block in divs:
                    ans = [] # это один из ответов
                    counter+=1
                    for inf_block in block: # заполняем ответ
                        ans.append(inf_block)
                    answers.append(ans)
                    if counter > reqData.ansNum:# если достаточно ответов
                        break 
                yield answers 
