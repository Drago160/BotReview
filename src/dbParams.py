class RequestData:
    
    def __init__(self, questNum, ansNum):
        self.questNum = questNum 
        self.ansNum = ansNum 
        self.askFlag = False
        self.howManyQuestFlag = False
        self.howManyAnsFlag = False

    def change(self, questNum, ansNum):
        self.questNum = questNum
        self.ansNum = ansNum

class Client:

    def __init__(self, my_id):
        self.askFlag = False
        self.howManyQuestFlag = False
        self.howManyAnsFlag = False
        self.id = my_id
        self.reqData = RequestData(3, 4) 


    def updateQuestNum(self, text):
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
        if text.isdigit():
            self.reqData.ansNum = max(int(text), 1)
            self.howManyAnsFlag = False 
            return True
        else:
            self.howManyQuestFlag = False 
            self.howManyAnsFlag = False 
            return False


