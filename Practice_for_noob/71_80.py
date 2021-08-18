#071
my_variable = ()
print(type(my_variable))

#072
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

#073
tuple_ = (1,)
print(type(tuple_))

#074
t = (1, 2, 3)
#t[0] = 'a'
# 튜플은 원소를 변경할 수 없다. 변경하려고 하려면  오류 발생!

#075
t = 1, 2, 3, 4
print(type(t))

#076
new_t = "a", "b", "c"
print(new_t)
new_t = "A", "b", "c"
print(new_t)
# 튜플은 원소의 값을 변경할 수 없기 때문에 새로운 튜플을 만들어서 new_t에 대입해줘야 한다.

#077
interest = ("삼성전자", "LG전자", "SK Hynix")
list_interest = list(interest)
print(type(list_interest))
# list()가 list로 만들어주는 함수인가부다

#078
tuple_interest = tuple(list_interest)
print(type(tuple_interest))
# 마찬가지로 tuple()은 tuple로 만들어주는 함수겠지!!

#079
temp = ("apple", "banana", "cake")
a, b, c = temp
print(a, b, c)
print(type(temp))

#080
even_tuple = tuple(range(2, 100, 2))
print(even_tuple)