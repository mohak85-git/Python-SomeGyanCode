import pytz
import datetime

naive_local_time = datetime.datetime.now()
naive_utc_time = datetime.datetime.utcnow()

print(f"Naive local time is {naive_local_time}")
print(f"Naive UTC time is {naive_utc_time}")

wrong_aware_local_time = pytz.utc.localize(naive_local_time)
# It is wrong to try to convert this way.
# Always convert utcnow time to local using localize and .astimezone()
proper_aware_local_time = pytz.utc.localize(naive_utc_time).astimezone()
aware_utc_time = pytz.utc.localize(naive_utc_time)

print(f"Wrong aware local time is {wrong_aware_local_time},"
      f"\n\t and timezone is: {wrong_aware_local_time.tzinfo}")
# notice that the timezone is shown wrongly as UTC.

print(f"proper aware local time is {proper_aware_local_time},"
      f"\n\t and timezone is: {proper_aware_local_time.tzinfo}")
print(f"aware UTC time is {aware_utc_time},"
      f"\n\t and timezone is: {aware_utc_time.tzinfo}")
