print("hello")
age =input("what is you current age")
age_as_int= int(age)
year=90-age_as_int
month=year*12
days=year*365
week=year*52
result=f"you have {year}year,{week}weeks,and {days}days,{month}months left.to survive"
print(result)