import re

txt = "HelloWorldExample"
x = re.sub(r'([A-Z])', r' \1', txt).strip()

print(x)
