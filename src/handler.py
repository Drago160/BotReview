import src.Toolfunc as Toolfunc
import re
import CONSTANT.py
class Handler:
    """Класс для обработки ответов с сайта"""

    def __init__(self):
    """Конструктор не принимает параметров"""
        pass

    def cleanStrFromTag(self, string, tag):
        """Метод очищает сообщение от полученного тега"""
        string = re.sub(r'\<'+tag+'[^>]*\>', '', string)
        string = re.sub(r'\</'+tag+'[^>]*\>', '', string)
        return string

    def cleanStrFromTags(self, string):
        """Метод очищает строку от всех тегов кроме Обрабатываемых телегой"""
        tags = re.findall(r'<([^\s/> ]+)', string)
        for tag in tags:
            if tag not in CONSTANT.NON_WORKED_TAGS:
                string = self.cleanStrFromTag(string, tag)
        return string

    def handle_answer(self, answer):
        """Метод Обрабатывает полученный Ответ"""
        ret =  str(answer)
        if len(ret)<2:
            return ret

        ret = self.cleanStrFromTags(ret)
        return ret

    def handle_answer_list(self, answers):
        """Метод обрабатывает список из полученных ответов"""
        return [self.handle_answer(ans) for ans in answers]


