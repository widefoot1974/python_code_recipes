import time
from datetime import datetime,timedelta


def delta_to_date(delta):
    t_days = delta.days
    t_hours = int(delta.seconds/3600)
    t_minutes = int((delta.seconds%3600)/60)
    t_seconds = int(delta.seconds%60)

    return (t_days, t_hours, t_minutes, t_seconds)

dt1 = datetime.now()
dt_str = dt1.strftime("%Y-%m-%d %H:%M:%S.%f")
print(f'지금 시각 : {dt_str}')

# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.microsecond)

after_days = 21
delta = timedelta(days=after_days)

dt2 = dt1 + delta
dt_str = dt2.strftime("%Y-%m-%d %H:%M:%S.%f")
print(f'지금부터 [{after_days}] 일 후 시간 : {dt_str}')

after_weeks = 21
delta = timedelta(weeks=after_weeks)

dt3 = dt1 + delta
dt_str = dt3.strftime("%Y-%m-%d %H:%M:%S.%f")
print(f'지금부터 [{after_weeks}] 주 후 시간 : {dt_str}')

birth_day = datetime(1975, 1, 30, 4, 0, 0)
dt_str = birth_day.strftime("%Y-%m-%d %H:%M:%S")
print(f'나의 생일은 {dt_str}')

while True:
    dt4 = datetime.now() - birth_day
    (t_d, t_h, t_m, t_s) = delta_to_date(dt4)
    print(f'내가 살아온 날은 {t_d:,}일 {t_h}시:{t_m}분:{t_s}초')
    time.sleep(10)


