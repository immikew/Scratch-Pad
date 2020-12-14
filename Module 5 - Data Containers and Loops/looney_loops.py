


if __name__ == "__main__":

    vowels = ('a', 'e', 'i', 'o', 'u')

    # i = 0
    # while i < len(vowels):
    #     print(vowels[i])
    #     i += 1

    # for letter in vowels:
    #     print(letter)


    # for i in range(10, 21, 2):
    #     print(i)

    for i in range(5):
        print('pre nested loop')
        for j in range(5, 8):
            print(f'i = {i}; j = {j}')

        print('post nested loop')

    print('script complete')