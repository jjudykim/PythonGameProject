#061
price = ["20180728", 100, 140, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
print(nums[1::2])

#064
nums2 = [1, 2, 3, 4, 5]
print(nums2[::-1])

#065
interest = ["삼성전자", "LG전자", "Naver"]
print(interest[0], interest[2])

#066
interest2 = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
print(" ".join(interest2))

#067
print("/".join(interest2))

#068
print("\n".join(interest2))

#069
string = "삼성전자/LG전자/Naver"
interest3 = string.split("/")
print(interest)

#070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)