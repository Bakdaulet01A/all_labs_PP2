import re

txt = "absatarov_bakdaulet_erkanatovich"
x = re.sub(r"[_]", '', txt)
print(x)
