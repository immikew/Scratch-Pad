
# Always put restrictive conditional at the top
def check_divisible_by_2_and_3(A):
    if A % 2 == 0 and A % 3 == 0:
        print(f'2 and 3 divides A ({A:02})!')
    elif A % 3 == 0:
        print(f'3 divides A ({A:02})!')
    elif A % 2 == 0:
        print(f'2 divides A ({A:02})!')
    else:
        print(f"2 or 3 doesn't divide A ({A:02})!")

for i in range(1, 11):
    check_divisible_by_2_and_3(i)