print('Welcome to the tip calculator')

bill = float(input('What was the total bill? $ '))
tip = int(input('How much tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

percent = tip/100
tip_amount = bill * percent
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f'Each person shoud pay ${final_amount}')
