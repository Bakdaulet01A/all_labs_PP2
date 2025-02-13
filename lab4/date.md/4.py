from datetime import datetime, timedelta

date1 = datetime.now()
date2 = datetime.now() - timedelta(1)
print(date1)
print(date2)
print(abs((date1 - date2).total_seconds()))
