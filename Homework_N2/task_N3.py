while True: # using while loop to make sure user puts correct years
    text = input("Enter a year").strip()
    try:
        year = int(text)
    except ValueError: # prints out warning to use a intiger(natural number)
           print("Invalid number. please enter a natural number")
           continue
    if year <= 0: # if statement if user puts a year that is less than 0 ( we only do AD sadly :( )
        print("Invalid number. please enter a number that is greater than 0")
        continue
    break
# Writing if else statement to make sure users year is leap year or not
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
   print(year, " is a leap year")
else:
    print(year, "is not a leap year")