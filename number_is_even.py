def isEven(value):
    """ Original function from the task """
    return value % 2 == 0


def number_is_even(value: int) -> bool:
    """ This function determines if a number is even """
    return int(bin(value)[-1]) == 0


if __name__ == "__main__":
    number = int(input("Введите целое число "))
    print(isEven(number))
    print(number_is_even(number))
