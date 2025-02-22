import re

txt = "abbb" 
x = re.fullmatch("ab{2,3}", txt)  
if x:
    print("YES")
else:
    print("NO")
