# debt calculator
def debt():
    total = []
    debts = {}
    

    # name = input("Enter debt name: ")
    # namedebt = float(input("Enter amount owed: "))
    # debts[name] = amount



    while True:
        name = input("Enter debt name (when finished enter done)")
        if name == "done":
                break
        try:
            amount = float(input("Enter amount owed: "))
            debts[name] = amount
           
        except:
            print("Enter a valid number")

        print("\n All debts:")
        for name, amount in debts.items():
            print(f"{name}: ${amount:.2f}")

    # adds all values
    total_sum = sum(debts.values())
    print(f"\n The total debt is: ${total_sum}")


    while True:
        try:
            monthly = input("Would you like to convert to monthly payments? Y/N: ").strip().lower()
            if monthly == "y":
                truly = int(input("How many months?").strip())


                divided = total_sum / truly
                print(f" Your monthly payments would be: {divided} \n Thank you for using the app!")
                break

            elif monthly == "n":
                print("Thank you for using the app!")
                break    

        except:
            print("Please enter Y or N.")

debt()