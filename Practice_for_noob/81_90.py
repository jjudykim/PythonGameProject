#081
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 하지만
# star expression(*)을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있다.
# 튜프에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코들르 작성할 필요가 없다.
a, b, *c = (0, 1, 2, 3, 4, 5, 6)
print(a, type(a))
print(b, type(b))
print(c, type(c))

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)
print(_)

#082
_, _, *valid_score = scores
print(valid_score)

#083
_, *valid_score, _ = scores
print(valid_score)

#084
temp = {}
print(type(temp))

#085
icecream = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(icecream)

#086
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500
print(icecream)

#087
print("메로나 가격: ", icecream["메로나"])

#088
icecream["메로나"] = 1300
print("메로나 가격: ", icecream["메로나"])

#089
del icecream["메로나"]
print(icecream)

#090
# 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생한다.