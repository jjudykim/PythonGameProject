#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#172
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])

#173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(len(price_list)-1-i, price_list[i])

#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(100 + 10*(i-1), price_list[i])

#175
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[i], my_list[i+1])

#176
my_list = ["가", "나", "다", "라", "마"]
for i in range(3):
    print(my_list[i], my_list[i + 1], my_list[i + 2])

#177
my_list = ["가", "나", "다", "라"]
for i in range(3, 0, -1):
    print(my_list[i], my_list[i-1])

#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1] - my_list[i])

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    sum_num = 0
    for j in range(3):
        sum_num += my_list[i+j]
    print(sum_num / 3)

#180
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(5):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)