print('This is the start of the file')

def calculate_weeks_pay(hours, hourly_pay):
    '''calculates the weeks pay

    Assumes that a 10% of the gross pay will be taken for payment of
    taxes.

    Parameters
    ----------
    hours : float
        the number of hours worked for the week
    hourly_pay : float
        the hourly payment

    Returns
    -------
    float
        the new pay expected'''
    print('This is the start of our function')
    gross_pay = hours * hourly_pay
    net_pay = gross_pay *.90
    return net_pay, gross_pay

print('Calling the function')
net_pay, gross_pay = calculate_weeks_pay(34.5, 16.25)

print(f'Your net pay is: ${net_pay:.2f}')
print(f'Your gross pay is: ${gross_pay:.2f}')
print('End')