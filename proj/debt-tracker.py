# debt calculator
def debt():
    total = []

    while True:
        raw_input = input(" Hi, what is the first amount you owe? (If done enter 0.): ")
        cleaned_input = raw_input.replace("$","").replace(",","").strip()
        try:
            amount = float(cleaned_input)
            if amount == 0:
                break
            total.append(amount)
            print(f"You added: $ {amount:.2f}")

        except:
            print("Enter a valid number")

    final_total = sum(total)
    print(f"\n Total debt: ${final_total:.2f}")


    while True:
        try:
            monthly = input("Would you like to convert to monthly payments? Y/N: ").strip().lower()
            if monthly == "y":
                truly = int(input("How many months?").strip())


                divided = final_total / truly
                print(f" Your monthly payments would be: {divided} \n Thank you for using the app!")
                break

            elif monthly == "n":
                print("Thank you for using the app!")
                break    

        except:
            print("Please enter Y or N.")

debt()