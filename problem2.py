"""
-------------------------------------------------------------------------------
Name: problem2.py
Purpose: Find when user reaches 100 km and how many days it took

Author: Koukoulidis.N

Created: 03/03/2021
------------------------------------------------------------------------------
"""

#title
print ("***** Welcome to the doordash distance tracker *****")
print("    ")
#travel log
print ("                  ** Travel Log **")
print(" ")

#Find how many days
total = 0
day = 0

while total <= 100 :
  amount = int(input("How far did you drive for the day?: "))
  total= total + amount
  day = day + 1

#summary
print("                     ** summary **")

print ("It took ", day , "days to pass 100km driven.")