import re
ret = "<div><b>Bold</b><a href=\"link\">content</a><strong>qwre</strong></div>"
ret = re.findall(r'<([^\s/>]+)',  ret) 
print(ret)
