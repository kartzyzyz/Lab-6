age = int(input("Enter your age:"))
is_member = input("Are you a member? (yes/no):")

if age < 18:
    if is_member == "yes":
        fee = 450
    else:
        fee = 650
elif 18 <= age <= 65:
    if is_member == "yes":
        fee = 550
    else:
        fee = 750
elif age > 65:
    if is_member == "no":
        fee = 400
    else:
        fee = 600
print(f"The Registration fee is {fee} pesos.")