import re

txt = "hello_world, world_hello, salam_aleikum, ualeikumassalam, kak_dela, horosho"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x)