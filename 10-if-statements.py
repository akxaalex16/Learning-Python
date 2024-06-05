# conditions:
# if it's a hot 
#    It's a hot day
#    Drink plenty of water
# otherwise if it's cold
#    It's a cold day
#    Wear warm clothes
# otherwise
#    It's a lovely day

is_hot=True
is_cold=False

if  is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

# challenge:
# Price of a house is $1M.
# If buyer has good credit,
#     They need to put down 10%
# Otherwise
#     They need to put down 20%
# Print the down payment

price= 1000000
good_credit= True

if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f'Down payment: ${down_payment}')