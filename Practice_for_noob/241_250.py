#241
import datetime
print(datetime.datetime.now())

#242
now = datetime.datetime.now()
print(now, type(now))

#243
now = datetime.datetime.now()
for day in range(5, 0, -1):
    delta = datetime.timedelta(days = day)
    date = now - delta
    print(date)

#244
print(now.strftime("%H:%M:%S"))

#245
day = "2021-08-27"
day_ = datetime.datetime.strptime(day, "%Y-%m-%d")
print(day_, type(day_))

#246
import time
import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

#247
# 모듈을 import 하는 4가지 방법

#248
import os
result = os.getcwd()
print(result, type(result))

#249
import os
os.rename(r"C:\Users\admin\Desktop\수강신청 계획.txt", r"C:\Users\admin\Desktop\done.txt")

#250
# 찾아보니까 numpy는 따로 설치를 해야한다고 하는구만,,
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)