# 9. Repeat the previous question but, this time, use augmented assignment 
# to compute the final result, one year at a time.

initial_balance = 1000
interest_rate = 0.05
interest_multiplier = 1 + interest_rate

balance = initial_balance * interest_multiplier
print(f'Bank balance at end of year 1: {balance}')

years = [2, 3, 4, 5]

for year in years:
    balance *= interest_multiplier
    print(f'Bank balance at end of year {year}: {balance}')
