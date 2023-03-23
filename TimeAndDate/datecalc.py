import time

print(time.gmtime(0))   # returns start of epoch time in UTC.

print(time.gmtime())    # returns current time, in UTC.

print(time.localtime(0))  # returns local time, when start of epoch.

print(time.localtime())  # returns current local time.

print(time.time())      # returns no of seconds elapsed from start of epoch.

print(time.localtime(time.time()))  # returns current local time.

print(time.gmtime(time.time()))  # returns current time, in UTC.
