import re


text = "In the face of ambiguity, refuse the temptation to guess."
m_list = re.findall("t.*\s", text)
print(m_list)

m_list = re.findall("t.*?\s", text)
print(m_list)