#091
inventory = {"메로나" : [300, 20],
             "비비빅" : [400,3],
             "죠스바" : [250, 100]}

#092
print(inventory["메로나"][0], "원")

#093
print(inventory["메로나"][1], "개")

#094
inventory["월드콘"] = [500, 7]
print(inventory)

#095
icecream = {"탱크보이" : 1200,
            "폴라포" : 1200,
            "빵빠레" : 1800,
            "월드콘" : 1500,
            "메로나" : 1000}
ice_keys = list(icecream.keys())
print(ice_keys)
# keys() 함수는 해당 딕셔너리의 키 값들을 반환한다

#096
ice_values = list(icecream.values())
print(ice_values)
# values() 함수는 해당 딕셔너리의 키에 대응하는 값들을 반환한다

#097
print(sum(ice_values))

#098
new_product = {"팥빙수" : 2700, "아맛나" : 1000}
icecream.update(new_product)
print(icecream)
#update(딕셔너리) 를 통해 다른 딕셔너리를 추가할 수 있음

#099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
print("zip 함수의 기능 :", zip(keys,vals), type(zip(keys,vals)))
print("dict 함수의 기능 : ", dict(zip(keys, vals)), type(dict(zip(keys, vals))))

#100
date = ["09/05", "09/06", "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)