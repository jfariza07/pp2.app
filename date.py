#task1
from datetime import datetime, timedelta

today = datetime.today()
five_days_ago = today - timedelta(days=5)
print("Five days ago:", five_days_ago.date())


#task2
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())


#task3
from datetime import datetime

now = datetime.now().replace(microsecond=0)
print("Datetime without microseconds:", now)


#task4
from datetime import datetime

date1 = datetime(2024, 2, 20, 12, 0, 0)  # Example date
date2 = datetime(2024, 2, 27, 12, 0, 0)  # Another example date

difference = abs((date2 - date1).total_seconds())
print("Difference in seconds:", difference)
