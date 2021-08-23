# #121
# input_char = input()
# if input_char.islower():
#     print(input_char.upper())
# else:
#     print(input_char.lower())
#
# #122
# user_score = int(input())
# if user_score >= 81 and user_score <= 100:
#     print("A")
# elif user_score >= 61 and user_score <= 80:
#     print("B")
# elif user_score >= 41 and user_score <= 60:
#     print("C")
# elif user_score >= 21 and user_score <= 40:
#     print("D")
# else:
#     print("E")
#
# #123
# exchange = { "달러" : 1167,
#              "엔" : 1.096,
#              "유로" : 1268,
#              "위안" : 171}
# user = input("입력 :")
# num, exchange_index = user.split()
# print(float(num) * exchange[exchange_index], "원")
#
# #124
# input_num1 = input("input number1:")
# input_num2 = input("input number2:")
# input_num3 = input("input number3:")
# if int(input_num1) >= int(input_num2) and int(input_num1) >= int(input_num2):
#     print(input_num1)
# elif int(input_num2) >= int(input_num1) and int(input_num2) >= int(input_num3):
#     print(input_num2)
# elif int(input_num3) >= int(input_num1) and int(input_num3) >= int(input_num2):
#     print(input_num3)
#
# #125
# 통신사 = {"011" : "SKT",
#        "016" : "KT",
#        "019" : "LGU",
#        "010" : "알 수 없음"}
# input_phone = input("휴대전화 번호 입력:")
# if input_phone[:3] in 통신사:
#     print("당신은", 통신사[input_phone[:3]], "사용자입니다." )
#
# #126
# input_num = input("우편번호:")
# check = int(input_num[2])
# if check in range(3):
#     print("강북구")
# elif check in range(3, 6):
#     print("도봉구")
# elif check in range(6, 10):
#     print("노원구")
#
# #127
# user_num = input("주민등록번호:")
# sex_num = int((user_num.split("-")[1])[0])
# if sex_num == 1 or sex_num == 3:
#     print("남자")
# elif sex_num == 2 or sex_num == 4:
#     print("여자")
#
# #128
# user_num = input("주민등록번호:")
# local_num = int((user_num.split("-")[1])[1:3])
# if local_num in range(0, 8):
#     print("서울입니다")
# else:
#     print("서울이 아닙니다.")
#
# #129
# user_num = input("주민등록번호:")
# user_num = user_num.replace("-", "")
# multi = "234567892345"
# sum = 0
# for i in range(len(multi)):
#     sum += int(user_num[i]) * int(multi[i])
# if user_num[-1:] == 11 - sum % 11:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

#130
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")