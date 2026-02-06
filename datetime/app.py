from datetime import datetime, timedelta
import time
# python 3 datetime -- google
dt = datetime


# date time object to string
print(dt)
print(dt.now())
print(dt.now().isoformat())
print(dt.now().strftime("%Y-%m-%d %H:%M:%S"))
print(dt.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(dt.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
timeMachine = dt.fromtimestamp(time.time())
print(timeMachine)


# string to date time object
dt_string = "2024-06-01 12:30:45"
dt_object = dt.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
print(dt_object)


# timedelta
dt1 = dt(2026, 1, 6) + timedelta(1)
dt2 = dt.now()

duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.total_seconds())
