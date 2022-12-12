import re


text = "In the face of ambiguity,  refuse the temptation to guess."
match_list = re.findall(" +[or]", text)
print(match_list)