import re

txt = "hello world, apple.banana fruits, data"
x = re.sub(r"[., ]", ':', txt )
print(x)