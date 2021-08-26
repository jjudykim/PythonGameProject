#211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
# 안녕
# Hi

#212
def 함수(a, b):
    print(a + b)

함수(3, 4)
함수(7, 8)
# 7
# 15

#213
# def 함수(문자열) :
#     print(문자열)
# 인자를 넣어줘야 하는 함수인데 인자를 넣어주지 않고 실행하려고 했다 이말이다~~

#214
# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)
# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 하려는 의도로 설계됐지만
# 함수를 호출할 때 문자열과 숫자를 입력했기 때문에 문자열과 숫자는 더할 수가 없는 에러가 뜬다

#215
def print_with_smile(string):
    print(string + ":D")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price(current):
    print(current + current*0.3)
print_upper_price(1000)

#218
def print_sum(a, b):
    print(a + b)
print_sum(3, 6)

#219
def print_arithmetic_operation(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

print_arithmetic_operation(3, 4)

#220
def print_max(a, b, c):
    if(a >= b and a >= c):
        print(a)
    elif(b >= a and b >= c):
        print(b)
    elif(c >= a and c >= b):
        print(c)

print_max(2, 7, 16)