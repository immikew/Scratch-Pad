def print_comparisons(A, B):
    print(f'{A} >  {B}: {A > B}')
    print(f'{A} <  {B}: {A < B}')
    print(f'{A} >=  {B}: {A >= B}')
    print(f'{A} <=  {B}: {A <= B}')
    print(f'{A} ==  {B}: {A == B}')
    print(f'{A} !=  {B}: {A != B}')

A = 'apples'
B = 'applesauce'

print_comparisons(A, B)

print('A ord : B ord')
for a_char, b_char in zip(A, B):
    print(f'{ord(a_char):<6}: {ord(b_char):>}')