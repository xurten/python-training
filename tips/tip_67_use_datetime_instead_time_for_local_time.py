# Tip 67 use datetime instead of time

import time

now = 1552774475
local_touple = time.localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
print(time.strftime(time_format, local_touple))