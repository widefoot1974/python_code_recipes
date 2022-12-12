import re

text = "Emma's luck number are 251 761 231 451"
pattern = r"\d{3}"
p = re.compile(pattern)

m = p.search(text)
if m:
    print(m.group())
else:
    print("not matched")

result = p.findall(text)
print(result)