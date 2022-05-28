# Creating a Tip Calculator
bill = float(input("What was the total bill? $"))
people = int(input("How many people are going to pay the bill?"))
tip = float(input("How much tip in percentage would you like to give?"))
final_bill = ((tip/100)*bill +bill)/people 
final_bill = round(final_bill,2)
print(f"Each person needs to pay ${final_bill}")


