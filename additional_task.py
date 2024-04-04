# Input - 34.34, 12.01, 17.42, 4.93
# Output_dollars - 68
# Outputs_cents - 70

bill_one = 34.34
bill_two = 12.01
bill_three = 17.42
bill_four = 4.93

final_bill =  bill_one + bill_two + bill_three + bill_four

dollars = int(final_bill)
cents = int((final_bill - int(final_bill)) * 100)

print(f"Price {final_bill}",f"Dollars {dollars}",f"Cents {cents}",sep='\n')