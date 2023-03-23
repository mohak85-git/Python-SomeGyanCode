import pytz
import datetime

# *** Print time in Moscow and UTC using pytz ***
# country = 'Europe/Moscow'
#
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print(f"The time in {country}, is {local_time}")
# print(f"UTC is {datetime.datetime.utcnow()}")

# *** print all timezones supported in pytz ***
# for x in pytz.all_timezones:
#     print(x)

# *** print all country codes supported in pytz ***
#  country_names returns country codes
# for x in pytz.country_names:  #  returns country codes only
#     print(x)

# *** print all country codes and corresponding country names supported in
# pytz ***
# for x in pytz.country_names:
    #  country_names[x] returns names of countries
    # print(x + ": " + pytz.country_names[x])

# *** print all country codes, corresponding country names and timezones
# supported in pytz ***
# for x in pytz.country_names:
#     print(f"{x}: {pytz.country_names[x]}: {pytz.country_timezones.get(x)}")

# *** print all country codes, corresponding country names, timezones and time
# supported in pytz ***

for x in pytz.country_names:
    print(f"{x}: {pytz.country_names[x]}", end=": ")
    if x in pytz.country_timezones:
        for zone in pytz.country_timezones[x]:
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print(f"\t\t{zone}: {local_time}")
    else:
        print("No timezone defined")
