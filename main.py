import random
from colorama import Fore
import os
secret_num = random.randint(1, 10)
run = True

def clearpage():
  os.system("cls||clear")

start = input(Fore.LIGHTBLUE_EX + "Guess the number (1 - 10)\n" + Fore.WHITE + "Press " + Fore.CYAN + "1" + Fore.WHITE + " to start: ")

if start == "1":
  
  clearpage()
  
  while run:
    second_run = True
    third_run = True
    attempt_1 = int(input("Enter your " + Fore.LIGHTGREEN_EX + "first" + Fore.WHITE + " guess: "))
    
    if attempt_1 == secret_num:
      print(Fore.GREEN + "\nCorrect!")
      run = False
    else:
      print(str(attempt_1) + " is " + Fore.LIGHTRED_EX + "incorrect.")
    
    while second_run and run:
      attempt_2 = int(input(Fore.WHITE + "\nEnter your " + Fore.LIGHTYELLOW_EX + "second" + Fore.WHITE + " guess: "))
          
      if attempt_2 == secret_num:
        print(Fore.GREEN + "\nCorrect!")
        run = False
        second_run = False
      elif attempt_2 == attempt_1:
        print("You cannot guess the same number twice.")
      else:
        print(str(attempt_2) + " is " + Fore.LIGHTRED_EX + "incorrect.")
        second_run = False
    
    while third_run and run:
      attempt_3 = int(input(Fore.WHITE + "\nEnter your " + Fore.RED + "final" + Fore.WHITE + " guess: "))
          
      if attempt_3 == secret_num:
        print(Fore.GREEN + "\nCorrect!")
        run = False
        third_run_run = False
      elif attempt_3 == attempt_1 or attempt_3 == attempt_2:
        print("You cannot guess the same number twice.")
      else:
        print(str(attempt_3) + " is " + Fore.LIGHTRED_EX + "incorrect.")
        print(Fore.WHITE + "\nThe " + Fore.GREEN + "correct " + Fore.WHITE + "number was " + str(secret_num))
        third_run_run = False
        run = False
     
