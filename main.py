print()

print("Think of either pizza, chair, cat, rock, or cloud.")
print("Enter yes or no to each of the questions, and I will guess what you chose.\n")

answer = input("Is it man-made? ")

if answer == "yes":
  answer = input("Is it edible? ")

  if answer == "yes":
    print("\nYou were thinking of a pizza 🍕")
  else:
    print("\nYou were thinking of a chair 🪑")
else:
  answer = input("Is it alive? ")

  if answer == "yes":
    print("\nYou were thinking of a cat 🐱")
  else:
    answer = input("Is it solid? ")

    if answer == "yes":
      print("\nYou were thinking of a rock 💎")
    else:
      print("\nYou were thinking of a cloud ☁")
