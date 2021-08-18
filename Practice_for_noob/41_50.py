#041
ticker = "btec_krw"
print(ticker.upper())

#042
ticker2 = "BTC_KRW"
print(ticker2.lower())

#043
a = "hello"
print(a.capitalize())

#044
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

#045
print(file_name.endswith("xlsx") or file_name.endswith("xls"))

#046
file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith("2020"))

#047
b = "hello world"
print(b.split())

#048
ticker3 = "btc_krw"
print(ticker3.split("_"))

#049
date = "2020-05-01"
sp_date = date.split("-")
year = sp_date[0]
month = sp_date[1]
day = sp_date[2]
print(year, month, day)

#050
data = "039490     "
print(data.rstrip())
