#021
letters = 'python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[-4:])

#023
string = "홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[::-1])

#025
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

#026
phone_number2 = "010-1111-2222"
print(phone_number2.replace("-", ""))

#027
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

#028
lang = 'python'
#lang[0] = 'p'
#문자열 수정 X
print(lang)

#029
string = "abcdfe2a354a32a"
string = string.replace("a", "A")
print(string)

#030
string = 'abcd'
string.replace('b', 'B')
print(string)
print(string.replace('b', 'B'))