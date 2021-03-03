"""
-------------------------------------------------------------------------------
Name: problem1.py
Purpose: find whether your team made it to which round.

Author: Koukoulidis.N

Created: 03/03/2021
------------------------------------------------------------------------------
"""

#ask user how many times they won
win = 0

for i in range (6):
  game = input ("Win or Loss (write W for wins and L for losses): ")
  if game == "W" or game == "w":
    win = win + 1


#Tell user which group they are in

if win == 0: 
  print ("Your team is eliminated from the tournament")
elif win == 1 or win == 2:
  print ("Your team is in group 3")
elif win == 3 or win == 4:
  print ("Your team is in group 2")
else: 
  print ("Your team is in group 1")




