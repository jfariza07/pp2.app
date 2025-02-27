from datetime import datetime, timedelta

today = datetime.today()
five_days_ago = today - timedelta(days=5)
print("Five days ago:", five_days_ago.date())
