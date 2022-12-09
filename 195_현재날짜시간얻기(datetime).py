from datetime import datetime


dt = datetime.now()
dt_str = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
print(dt_str)

print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

