import random
import time    # Import time library (time.sleep()) for make the code output more realistic making user's actions wait for a few seconds

a = random.randint(1,9)
b = random.randint(1,9)
c = random.randint(1,9)  # Creating 3 random numbers using variables "a", "b" and "c"
time.sleep(1)
username = input ("Enter your Username: ")
time.sleep(2)
usd_amount = int(input("Enter the amount of money you want to spin (Minimum 10$): "))

while usd_amount >= 1:   # While the amount is to the limit (and above), the user can start to "spin"
    print ("###################")
    print("Your Balance:", usd_amount)
    print ("###################")
    print ()
    time.sleep(2)
    spin = input("[SPIN THE WHEEL]")
    time.sleep(2)
    print ("=========")
    print(a, "|", b, "|", c)
    print ("=========")
    usd_amount = usd_amount - 1
    if a == 5 and b == 5 and c == 5:
        usd_amount += 500
        time.sleep(1)
        print ("* You won 500$ *")
        print ()
        time.sleep(2)
        print("------------------------------------")
        print()
    elif a == 7 and b == 7 and c == 7:
        usd_amount += 1000
        time.sleep(1)
        print("* You won 1000$ *")
        print()
        time.sleep(2)
        print ("------------------------------------")
        print()
    elif a == 9 and b == 9 and c == 9:
        usd_amount += 5000
        time.sleep(1)
        print ("* You won 5000$ *")
        print ()
        time.sleep(2)
        print("------------------------------------")
        print()
    else:
        time.sleep(1)
        print ("* You didn't win anything *")
        time.sleep(2)
        print ()
        time.sleep(2)
        print("------------------------------------")
        print()
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)

print ("You're out of cash")
