#Creating first and second word input
first = input("Input:\n")
second = input()
#using if statement to see if we can use first words to create a second word
if sorted(first.lower()) == sorted(second.lower()):
    print("YES")
else:
    print("NO")
