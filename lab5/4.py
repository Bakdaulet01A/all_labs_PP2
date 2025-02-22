import re

txt = "Absatarov, Hello, Bakdaulet, apple, banana"
x = re.findall(r"\b[A-Z][a-z]+", txt)
print(x)