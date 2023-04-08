happy_ticket = input("input 6digit number ")
first_three_digits = int(happy_ticket[0])+int(happy_ticket[1])+int(happy_ticket[2])
last_three_digits = int(happy_ticket[3])+int(happy_ticket[4])+int(happy_ticket[5])
if first_three_digits == last_three_digits:
    print("yes")
else:
    print("no")