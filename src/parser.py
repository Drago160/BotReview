from bs4 import BeautifulSoup as BS
import requests
from googlesearch import search
import src.Toolfunc as Toolfunc 

class Parser:

    def __init__(self):
        pass

    def find_answers(self, Error_name, num = 3):
        ip = Error_name + "python stacoverflow"

        for url in search(ip, stop=3):
            if url.find("stackoverflow"): 
                print(url)
                page = requests.get(url)
                soup = BS(page.text, "html.parser")
                divs = soup.find_all("div", attrs= {"itemprop":"text"})

                answers = []

                counter = 0
                for c in divs:
                    ans = []
                    counter+=1
                    for i in c:
                        ans.append(i)
                    answers.append(ans)
                    if counter >= num:
                        break
        return answers
                
