#181
apart = [["101호", "102호"],["201호", "202호"],["301호", "302호"]]
print(apart)

#182
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
print(stock)

#183
stock = {"시가" : [100, 200, 300],
         "종가" : [80, 210, 330]}
print(stock)

#184
stock = {"10/10" : [80, 110, 70, 90],
         "10/11" : [210, 230, 190, 200]}
print(stock)

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(len(apart)):
    for j in range(len(apart[0])):
        print(f"{apart[i][j]} 호")
# 더 쉬운 방법
for row in apart:
    for col in row:
        print(col, "호")

#186
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row:
        print(col, "호")

#187
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")

#188
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
        print("-----")

#189
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
    print("-----")

#190
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
print("-----")