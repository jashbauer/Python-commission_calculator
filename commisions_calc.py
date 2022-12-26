
# SALES COMMISSION CALCULATOR
while True:
    name = input("Please, enter your name: ")

    try:
        sales = float(input("Please, enter your sales value in $: "))
        if sales < 0:
            print("You cannot enter a negative value.")
        else:
            comm = sales*0.13
            print(f"{name}, you've earned ${comm:.2f} this month. Enjoy!")

    except ValueError:
        print("Invalid amount. Enter amount as a number (float)")
    finally:
        print("Thank you for using the calculator.\n\n")

    quit = input("press 'q' to quit: ")
    if quit == "q":
        break
