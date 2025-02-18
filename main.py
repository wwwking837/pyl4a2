# Factorial of a number using recursion
def recur_factorial(n) :
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
num= int(input("Enter a number"))

#check if the number is positive
if num < 0:
    print("Sorry factorial doesn't exist")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
