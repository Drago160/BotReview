class RequestData:
    """Класс содержит информацию о запросе который формируется"""

    def __init__(self, questNum, ansNum):
        """Конструктор принимает кол-во искомых запросов на сайт
        и кол-во отображаемых ответов"""
        self.questNum = questNum 
        self.ansNum = ansNum 
        self.askFlag = False
        self.howManyQuestFlag = False
        self.howManyAnsFlag = False

    def change(self, questNum, ansNum):
        """Метод изменяет кол-во искомых запросов на сайт и 
        кол-во отображаемых ответов"""
        self.questNum = questNum
        self.ansNum = ansNum

class Client:
    """Аккаунт собеседника"""

    def __init__(self, my_id):
        """Конструкто принимает id собеседника"""
        self.askFlag = False
        self.howManyQuestFlag = False
        self.howManyAnsFlag = False
        self.id = my_id
        self.reqData = RequestData(3, 4) 


    def updateQuestNum(self, text):
        """Метод меняет кол-во искомых запросов"""
        if text.isdigit():
            self.reqData.questNum = int(text)
            self.howManyQuestFlag = False 
            self.howManyAnsFlag = True 
            return True
        else:
            self.howManyQuestFlag = False 
            self.howManyAnsFlag = False
            return False


    def updateAnsNum(self, text):
        """Метод меняет кол-во ответов на запросы"""
        if text.isdigit():
            self.reqData.ansNum = max(int(text), 1)
            self.howManyAnsFlag = False 
            return True
        else:
            self.howManyQuestFlag = False 
            self.howManyAnsFlag = False 
            return False


