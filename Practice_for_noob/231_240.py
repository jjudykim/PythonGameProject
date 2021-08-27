#231
def n_plus_1 (n):
    result = n + 1

n_plus_1(3)
#print(result)

#232
def make_url(string):
    print(f"www.{string}.com")

make_url("naver")

#233
def make_list(string):
    list_ = []
    for i in range(len(string)):
        list_.append(string[i])
    return list_
# 더 쉬운 방법
def make_list2(string):
    return list(string)

print(make_list("abcd"))
print(make_list2("abcd"))

#234
def pickup_even(list_):
    temp_list = []
    for i in list_:
        if i % 2 == 0:
            temp_list.append(i)
    return temp_list

print(pickup_even([3, 4, 5, 6, 7, 8]))

#235
def convert_int(string):
    return int(string.replace(",", ""))

print(convert_int("1,234,567"))

#236
def 함수(num):
    return num + 4

a = 함수(10)
b = 함수(a) # 함수(14)
c = 함수(b) # 함수(18)
print(c)

#237
def 함수(num):
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)  #14
c = 함수2(a)   #140
print(c)

#239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)    #함수1(12)

c = 함수2(10)  #16
print(c)

#240
def 함수0(num) :
    return num * 2
def 함수1(num) :
    return 함수0(num + 2)
def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)  # 함수1(12) -> 함수0(14) -> 28
print(c)
