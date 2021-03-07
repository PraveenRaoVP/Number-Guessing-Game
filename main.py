from random import *
import os
def assignNumber():
     return randint(1,100)

def main():
     lowRange=0
     highRange=100
     print("A random number has been selected by me for you to find. Find out the number within 10 choices!")
     count=1
     findNumber=assignNumber()
     while(True):
          n=int(input(f"Enter a number in the range {lowRange},{highRange} : "))
          if(n>100):
               print("The number must be within 0 to 100. Try again")
               main()
          if(n<findNumber):
               print("The number you have entered is lower than my number. Try again")
               count+=1
               if(n>lowRange):
                    lowRange=n
          if(n>findNumber):
               print("The number you have entered is greater than my number. Try again")
               count+=1
               if(n<highRange):
                    highRange=n
          if(count>10):
               print(f"Sorry. You did not find the number within 10 tries. The number I was thinking of was {findNumber}.")
               choice=input("Do you want to try again? (y/n): ")
               if(choice=='y'):
                    os.system('cls')
                    main()
               else:
                    exit(0)
          if(n==findNumber):
               print(f"Congratulations! You have found my number in {count} times. ")
               choice=input("Do you want to continue(y/n) : ")
               if(choice=='y'):
                    os.system('cls')
                    main()
               else:
                    return False
               os.system('cls')
     exit(0)
     
main()
