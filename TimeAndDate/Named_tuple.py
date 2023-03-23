import time

time_here = time.localtime()
print(time_here)

# Demonstrate named tuple: struct_time()
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

#           OR

year, month, day_of_month, hour, minutes, seconds, day_of_week, day_of_year, \
    is_dst = time.localtime()

print(year, month, day_of_month, hour, minutes, seconds, day_of_week,
      day_of_year, is_dst, sep='\n')
