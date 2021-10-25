import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()  # 0 -> 星期一
print(now)

date_of_birth = dt.datetime(year=1993, month=8, day=25)
print(date_of_birth)

