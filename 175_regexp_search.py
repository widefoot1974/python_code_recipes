import re


text = "Errors should never pass silently."
m_obj = re.search(r"(n....)\s(p...)", text)
print(m_obj.group(0))
print(m_obj.group(1))
print(m_obj.group(2))
print(m_obj.groups())
