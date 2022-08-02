def quick_sort(numbers: list) -> list:
    """ This function sorts the list, by merge algorithm """
    if len(numbers) < 2:
        return numbers
    goal = numbers[0]
    less, greater = [], []
    for number in numbers[1:]:
        if number <= goal:
            less.append(number)
        else:
            greater.append(number)
    return quick_sort(less) + [goal] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([4, 2, 5, 7, 3, 12, 1, 54, 3, -45]))
