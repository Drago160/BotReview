class RequestData:
    
    def __init__(self, questNum, ansNum):
        self.questNum = questNum 
        self.ansNum = ansNum 

    def change(self, questNum, ansNum):
        self.questNum = questNum
        self.ansNum = ansNum

class Client:
    def __init__(self, my_id):
        self.id = my_id
        self.reqData = RequestData(3, 4)   
