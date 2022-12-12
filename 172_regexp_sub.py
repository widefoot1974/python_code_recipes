import re


text = "Beautiful is better than ugly."
replaced = re.sub("\s", "_", text)
print(replaced)