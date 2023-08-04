# making calculator using simple method


first_number=float(input("enter first number; "))

operator=input("enter operator(+,-,*,/); ")

second_number=float(input("enter secound number; "))

if operator== "+":
    print(first_number + second_number)

elif operator== "-":
    print(first_number - second_number)

elif operator== "*":
    print(first_number * second_number)


elif operator=="/":
    print(first_number / second_number)

else:
    print("invalid opperation")

