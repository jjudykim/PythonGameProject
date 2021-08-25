#161
for i in range(0, 100):
    print(i)

#162
for i in range(2002, 2051, 4):
    print(i)

#163
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

#164
for i in range(99, -1, -1):
    print(i)

#165
for i in range(10):
    print(i/10)

#166
for i in range(1, 10):
    print(f"3x{i} = {3*i}")

#167
for i in range(1, 10, 2):
    print(f"3x{i} = {3*i}")

#168
sum_i = 0
for i in range(1, 11):
    sum_i += i
print(f"합 : {sum_i}")

#169
sum_i_hol = 0
for i in range(1, 11, 2):
    sum_i_hol += i
print(f"합 : {sum_i_hol}")

#170
multi = 1
for i in range(1, 11):
    multi *= i
print(f"곱 : {multi}")