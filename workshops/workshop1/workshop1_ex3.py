import numpy as np

def tax(inc):

    if inc <= 300_000:
        amount = 0
        print("No tax!")
    elif inc <= 700_000:
        amount = (inc - 300_000) * 0.2
        print(f"Your tax is {amount}")
    else:
        amount = (700_000 - 300_000) * 0.2 + (inc - 700_000) * 0.35
        print(f"Your tax is {amount}")

    return amount

#inc = float(input("Write income here: "))
#tax(inc)

incomes = np.linspace(0, 1_200_000, 13)

taxes_loop =[]

for income in incomes:
    # Compute taxes for current income level
    taxes = tax(income)
    # Append to list
    taxes_loop.append(taxes)
    #Income after tax
    net_income = income - taxes

    print(f'Gross income: {income: 10.0f};'
            f'Taxes: {taxes:10.0f};'
            f'Net_income: {net_income:10.0f}')
    
    


