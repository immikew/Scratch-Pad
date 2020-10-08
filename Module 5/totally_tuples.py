

if __name__ == "__main__":

    # my_tuple = (1, '2.0', 3.0, (4, 5))
    # print(my_tuple)

    # print(my_tuple[0])
    # print(my_tuple[1])
    # print(my_tuple[2])
    # print(my_tuple[3])

    hello = "Hello there"
    my_tuple = tuple(hello)
    print(my_tuple)

    # query = (4, 5)
    # print(f'"{query}" is in my_tuple?: {query in my_tuple}')

    for letter in my_tuple:
        print(letter)

    print('script complete')