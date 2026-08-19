#program to generate bill
i1=str(input("enter 1st product"))
p1=float(input("enter the price of item"))
q1=int(input("enter the number of items"))

i2=str(input("enter 2nd product"))
p2=float(input("enter the price of item"))
q2=int(input("enter the number of items"))

i3=str(input("enter 3rd product"))
p3=float(input("enter the price of item"))
q3=int(input("enter the number of items"))

i4=str(input("enter 4th product"))
p4=float(input("enter the price of item"))
q4=int(input("enter the number of items"))
#total amount
total_bill=(q1*p1)+(q2*p2)+(q3*p3)+(q4*p4)

#format of the bill
print("############################################################ BILL ########################################################################")
print("Item name\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\fitem quantity\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\fitem price\f\f\f\f\f\f\f\f\f\f\f\f\f\f")
print("{i1}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{q1}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{p1}\f\f\f\f\f\f\f\f\f\f\f\f\f\f")
print("{i2}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{q2}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{p2}\f\f\f\f\f\f\f\f\f\f\f\f\f\f")
print("{i3}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{q3}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{p3}\f\f\f\f\f\f\f\f\f\f\f\f\f\f")
print("{i4}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{q4}\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f\f{p4}\f\f\f\f\f\f\f\f\f\f\f\f\f\f")
print("Total Bill Amount:",total_bill)
