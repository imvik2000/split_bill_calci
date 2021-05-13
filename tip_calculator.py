
def bill(total,tips):
    return(tips/100)*total +total

def split(persons,final_bills):
    return(final_bills/persons)

print("welcome to the tip calculator")
total_bill=float(input("enter the total bill in $"))
tip=int(input("enter the tip  in percentage without giving percent sign "))

final_bill=bill(total_bill,tip)

person=int(input("how many person to split the bill?"))

per_person_pay=split(person,final_bill)
per_person_pay= "{:.2f}".format(per_person_pay)  #  to round the bill amount with 2 decimal place 
print(f"total amount each person will pay ${per_person_pay}")

