#261
class Stock:
    pass

#262
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")
print(삼성.name, 삼성.code)

#263
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name, a.code)

#264
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

a = Stock(None, None)
a.set_code("005930")
print(a.name, a.code)

#265
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.get_name(), 삼성.get_code())

#266
class Stock:
    def __init__(self, name, code, PER, PBR, fee):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.fee = fee

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

#267
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.name, 삼성.code, 삼성.PER, 삼성.PBR, 삼성.fee)

#268
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def print(self):
        print(self.name, self.code, self.per, self.pbr, self.dividend)

#269
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.print()
삼성.set_per(12.75)
삼성.print()

#270
종목 = []

종목.append(Stock("삼성전자", "005930", 15.79, 1.33, 2.83))
종목.append(Stock("현대차", "005380", 8.70, 0.35, 4.27))
종목.append(Stock("LG전자", "066570", 317.34, 0.69, 1.37))

for i in 종목:
    print(i.code, i.per)