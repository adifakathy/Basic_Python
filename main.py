#Input from user and print system in python
import cell as cell

project_name = "This is the basic python syntex"
name = input ("enter your name:")
Address = input("Enter address:")
Phone_No="01787719946"
print(project_name)
print("Name :"+name)
print("Address :"+Address)
print("My contact no is:"+Phone_No)
#Type casting
a =int(input("enter the 1st number:"))
b =int(input("enter the 2nd number:"))
sum = a+b
sub =a-b
mul =a*b
div =a/b
mod =a%b
print("the sum is:",sum)
print("the sub is:",sub)
print("the mul is:",mul)
print("the div is:",div)
print("the mod is:",mod)
#Tuple is show in ()
'''
Tuple_list=("Riya(0)",234(1),"Ome(2)",937(3))
'''
tuple =("Riya",234,"Ome",937)
print(tuple)
# zero positional number will show in output
print(tuple[0])
#1 to 2 positional number will show in output
print(tuple[1:3])
# after 2 positional number will show in output
print(tuple[2:])
#List is show in []
List = ["Bina",234,"mira",848,"lina"]
tinylist =["mili",111]
print(List)
print(len(List))
print(tinylist*2)
print(List+tinylist)
#Libery Function
from math import *
print(round(3.8))
print(sqrt(25))
print(abs(-3))
print(pow(2,5))








