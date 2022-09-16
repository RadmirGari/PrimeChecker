#Write your code below this line 👇
import math
yes = "yes"
def prime_checker(number):
    hell = 0
    litu = []
    half = math.floor(number / 2)
    for digits in range(half):
        digits = digits + 1
                
        modulo = number % digits
        if modulo == 0:
             if digits == 1:
                digits - 1
                print("1")
             else:
                litu.append(digits)
                hell += 1
    if hell == 0:
        print(f"Number {number} is prime.")
    else:
        print(f"Not prime. Number {number} is divisable by number(s) {litu}")
        
        





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
while yes == "yes":
    n = int(input("Check this number: "))
    prime_checker(number=n)
    yes = input("Do you want to check another number? Yes or No:\n").lower()
print("Cya later alligator!")

