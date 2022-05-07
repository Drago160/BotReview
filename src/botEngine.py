from src.parser import Parser
from src.handler import Handler
from src.Toolfunc import str_sum
from src.dbParams import RequestData

class Engine():

    def __init__(self):
        self.parser = Parser()
        self.handler = Handler()
        self.num = 2
   
    def define(self, message):
        return True

    def find_answer_on_error(self, error_name, reqData):
        for answers_tag in self.parser.find_answers(error_name, reqData):
            yield (str_sum(self.handler.handle_answer_list(answer)) for answer in answers_tag)

