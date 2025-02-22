import re

txt = "banana"
x = re.search(r'a*b', txt)
if x:
    print("YES")
else:
    print("NO")