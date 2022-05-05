import src.Toolfunc as Toolfunc
import re
class Handler:

    def __init__(self):
        pass

    def handle_answer(self, answer):
        ret =  str(answer)
        if len(ret)<2:
            return ret

        #ret = ret.replace('<p>', '')
        #ret = ret.replace('</p>', '')
        #ret = ret.replace('<pre>', '')
        #ret = ret.replace("</pre>", '')
        #ret = ret.replace('<code>', '')
        #ret = ret.replace('</code>', '')
        #ret = ret.replace('<blockquote>', '')
        #ret = ret.replace('</blockquote>', '')
        #if ret[1] == "a":
        #    ret = ret[ret.find("href")+6:ret.find("\"", ret.find("href")+6, len(ret))]
        
        href = ret[ret.find("href")+6:ret.find("\"", ret.find("href")+6, len(ret))]
        print(href)
        arr2 = re.sub(r'<a[^>]*>([^<]+)</a>', href, ret)
        print()

        arr = re.findall(r'(?<=<p>)(.*)(?=</p>)', ret)
        arr1 = re.findall(r'(?<=<b>)(.*)(?=</b>)', ret)

        arr = arr + arr1

        if len(arr) > 0:
            ret = Toolfunc.str_sum(arr)
        return ret

    def handle_answer_list(self, answers):
        return [self.handle_answer(ans) for ans in answers]


