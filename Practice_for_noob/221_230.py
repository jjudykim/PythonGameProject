#221
def print_reverse(string):
    print(string[::-1])

print_reverse("python")

#222
def print_score(list_):
    sum = 0
    for i in list_:
        sum += i
    print(sum / len(list_))

print_score([1, 2, 3])

#223
def print_even(list_):
    for i in list_:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(dict_):
    for i in dict_:
        print(i)

print_keys({"이름":"김말똥", "나이":30, "성별":0})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(dict_, key_):
    print(dict_[key_])

print_value_by_key(my_dict, "10/26")

#226
def print_5xn(string):
    for i in range(len(string)):
        if i % 5 == 0:
            print("\n", end="")
        print(string[i], end="")

print_5xn("아이엠어보이유알어걸")

#227
def print_mxn(string, index):
    for i in range(len(string)):
        if i % index == 0:
            print("\n", end = "")
        print(string[i], end = "")

print_mxn("아이엠어보이유알어걸", 3)
print()

#228
def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))

calc_monthly_salary(12000000)

#229
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a = 100, b = 200)

#230
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b = 100, a = 200)