n = int(input("Enter a number: "))

while n < 1 or n > 1000: # using while loop to make sure user runs a natural number between 1 and 1000
    print("Please enter a  natural number between 1 and 1000")
    n = int(input("Enter a number: "))
#Creating divsions list and using for loop to add the numbers that is divsiors for n number
divisors = []
for i in range(1, n+1):
    if n % i == 0:
        divisors.append(str(i))
#Print out divisors
print(" ".join(divisors))