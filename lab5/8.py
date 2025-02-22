import re

txt = "HelloWorldExample"
x = re.findall(r'[A-Z][a-z]*', txt)

print(x)
