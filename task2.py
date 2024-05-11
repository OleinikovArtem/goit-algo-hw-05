def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return (iterations, arr[mid])

    if low < len(arr):
        return (iterations, arr[low])
    else:
        return (iterations, arr[-1])


def main():
    arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
    print(binary_search(arr, 3.5))  # Виведе: (кількість ітерацій, верхню межу)
    print(binary_search(arr, 4))  # Виведе: (кількість ітерацій, верхню межу)
    print(binary_search(arr, 6.0))  # Виведе: (кількість ітерацій, макс елемент)


if __name__ == "__main__":
    main()
