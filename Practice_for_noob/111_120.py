#111
user_input = input("입력 :")
print(user_input * 2)

#112
num = input("숫자를 입력하세요: ")
print(int(num) + 10)

#113
num_1 = input()
if int(num_1) % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
num_2 = input("입력값: ")
if int(num_2) + 20 > 255:
    print("255")
else:
    print(int(num_2) + 20)

#115
num_3 = input("입력값: ")
if int(num_3) - 20 < 0:
    print("0")
elif int(num_3) - 20 > 255:
    print("255")
else:
    print(int(num_3) - 20)

#116
time = input("현재시간:")
if time[-2:] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다")

#117
fruit = ["사과", "포도", "홍시"]
input_fruit = input("좋아하는 과일은? ")
if input_fruit in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user_jongmok = input("종목명 : ")
if user_jongmok in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input_season = input("제가좋아하는계절은:")
if input_season in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")


#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input_fruit = input("좋아하는과일은?")
if input_fruit in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")
