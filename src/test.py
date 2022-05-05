import re
st = "qwer<a href = "">qwerty</a>qwer"
arr2 = re.findall(r'<a[^>]*>([^<]+)</a>', st)
print(arr2)
