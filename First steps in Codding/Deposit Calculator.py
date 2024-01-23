amount_deposited = float(input())
term_deposit = float(input())
annual_interest_rate = float(input()) / 100

sum = amount_deposited + term_deposit * ((amount_deposited*annual_interest_rate)/12)

print(sum)