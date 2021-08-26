#191
data = [[ 2000,  3050,  2050,  1980],
        [ 7500,  2050,  2050,  1980],
        [15450, 15050, 15550, 14900]]
fee = 0.00014
for row in data:
    for col in row:
        print(col + col * fee)

#192
data = [[ 2000,  3050,  2050,  1980],
        [ 7500,  2050,  2050,  1980],
        [15450, 15050, 15550, 14900]]
fee = 0.00014
for row in data:
    for col in row:
        print(col + col * fee)
    print("-----")

#193
data = [[ 2000,  3050,  2050,  1980],
        [ 7500,  2050,  2050,  1980],
        [15450, 15050, 15550, 14900]]
fee = 0.00014
result = []
for row in data:
    for col in row:
        result.append(col + col * fee)
print(result)

#194
data = [[ 2000,  3050,  2050,  1980],
        [ 7500,  2050,  2050,  1980],
        [15450, 15050, 15550, 14900]]
fee = 0.00014
result = []
for row in data:
    temp = []
    for col in row:
        temp.append(col + col * fee)
    result.append(temp)
print(result)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])

#196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] > 150 : print(i[3])

#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[0] <= i[3] :
        print(i[3])

#198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for i in ohlc[1:]:
    volatility.append(i[1] - i[2])
print(volatility)

#199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] > i[0]:
        print(i[1] - i[2])

#200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
sum = 0
for i in ohlc[1:]:
    sum += i[3] - i[0]
print(sum)