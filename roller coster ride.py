print("Welcome to the rollercoaster!")
height = int(input("Can you tell me your height in CM? "))
bill = 0

# the criteria for height is maximum 120
if height > 120:
    print("Hurahhh!!You can ride the roller coaster")
    
    age = int(input("Enter Your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age == 12 or age < 18:
        bill = 7
        print("Your bill is $7")
    elif age >= 45 and age <= 55:
        print("Congratulations!! You got a free ride")
    else:
        bill = 12
        print("Adult tickets are 12$")
    
    want_photos = input("Do you want photos?? press Y for yes and N for no "
    "")
    if want_photos == "Y":
        bill += 3

    print(f"Your bill is ${bill}")
else:
    print("Oopss!! Sorry you have to grow your height")
