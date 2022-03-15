import datetime
import time


for i in range(20):
    now = datetime.datetime.now()
    now = time.strftime("%Y%M%d_%H%M%S")

    print(now)
    time.sleep(1)