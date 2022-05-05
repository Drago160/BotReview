import src.Toolfunc as Toolfunc
import re
class Handler:

    def __init__(self):
        pass

    def cleanStrFromTag(self, string, tag):
        string = re.sub(r'\<'+tag+'[^>]*\>', '', string)
        string = re.sub(r'\</'+tag+'[^>]*\>', '', string)
        return string

    def cleanStrFromTags(self, string):
        tags = re.findall(r'<([^\s/> ]+)', string)
        for tag in tags:
            if tag not in ['b', 'code', 'i', 'a', 'pre', 'strong']:
                string = self.cleanStrFromTag(string, tag)
        return string

    def createLink(self, string):
        all_hrefs = re.findall(r'a\s.*?href="(.+?)".*?>(.+?)</a>', ret)
        string = ""
        if len(href) > 0:
            for href, label in href:
               print("hi") 

    def handle_answer(self, answer):
        ret =  str(answer)
        if len(ret)<2:
            return ret

        ret = self.cleanStrFromTags(ret)
        return ret

    def handle_answer_list(self, answers):
        return [self.handle_answer(ans) for ans in answers]


