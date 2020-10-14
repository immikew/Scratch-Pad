
GROSS_PAY_DEFAULT = 500.0
grosspay = 500.0

def caluclate_weeks_pay(hours, pay):
    grosspay = hours * pay
    print(f'grosspay AFTER assignment in function: {grosspay}')
    netpay = grosspay * .90
    return netpay, grosspay

print(caluclate_weeks_pay(30, 15.25))

print(f'gross pay AT END: {grosspay}')