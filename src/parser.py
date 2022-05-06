from bs4 import BeautifulSoup as BS
import requests
from googlesearch import search
import src.Toolfunc as Toolfunc 

class Parser:

    def __init__(self):
        pass

    def find_all_blocks(self, url):
        page = requests.get(url)
        soup = BS(page.text, "html.parser")
        divs = soup.find_all("div", attrs= {"itemprop":"text"})
        return divs


    def find_answers(self, Error_name, num = 5):
        ip = Error_name + "python stacoverflow"
        # Перебираем url'ы
        for url in search(ip, stop=2):
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
                    if counter >= num:# если уже достаточно ответов для нас
                        break 
                yield answers 