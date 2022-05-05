from src.parser import Parser
from src.handler import Handler

def str_sum(strings):
    ret = ""
    for s in strings:
        ret += s
    return ret

class Engine():

    def __init__(self):
        self.parser = Parser()
        self.handler = Handler()
   
    def define(self, message):
        return True

    def find_answer_on_error(self, error_name):
        answers_tag = self.parser.find_answers(error_name)
        for answer in answers_tag:
            yield str_sum(self.handler.handle_answer_list(answer))
