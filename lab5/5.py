import re

txt = "hhakdauleb"
x = re.findall(r"a.*b$", txt)
print(x)