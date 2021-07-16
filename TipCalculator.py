# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:34:08 2021

@author: nishchay
"""


#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the Tip Calculator\n")

Total_bill = float(input("What was the total bill? $"))
Total_people = float(input("How many people to split the bill? "))
Percentage_tip = float(input("What percentage tip would you like to give? \n"))

Split  = Total_bill/Total_people
Split_per = (Split*Percentage_tip)/100
Final_split = Split+Split_per

final_amount = round(Final_split,2)
print(f"Each Person should pay: ${final_amount}")



x = input("Enter any number: ")

x_one = int(x[0])
x_two = int(x[1])


print(x_two+x_one)