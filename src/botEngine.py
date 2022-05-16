from src.parser import Parser
from src.handler import Handler
from src.Toolfunc import str_sum
from src.dbParams import RequestData

class Engine():
    """Контролирует все нетривиалные опирации бота"""
    def __init__(self):
        """Конструктор создает Engine не принимая параметров"""
        self.parser = Parser()
        self.handler = Handler()
        self.num = 2
   
    def define(self, message):
        """Метод проверяет является ли данный запрос об ошибке валидным"""
        return True

    def find_answer_on_error(self, error_name, reqData):
        """Метод ищет ответ по запросу find"""
        for answers_tag in self.parser.find_answers(error_name, reqData):
            yield (str_sum(self.handler.handle_answer_list(answer)) for answer in answers_tag)


