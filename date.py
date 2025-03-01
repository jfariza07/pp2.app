#task1
from datetime import datetime, timedelta

td = datetime.today()
five = td - timedelta(days=5)
print(five.date())


#task2
from datetime import datetime, timedelta

td = datetime.today()
ye = td - timedelta(days=1)
tm = td + timedelta(days=1)

print(ye.date())
print(td.date())
print(tm.date())


#task3
from datetime import datetime

now = datetime.now().replace(microsecond=0)
print(now)


#task4
from datetime import datetime

d1 = datetime(2025, 2, 23, 18, 0, 0)
d2 = datetime(2025, 2, 25, 18, 0, 0)

difference = abs((d2 - d1).total_seconds())
print(difference)
