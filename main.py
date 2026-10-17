def find_min_difference(arr):
    n = len(arr)
    if n < 2:
        return None

    # Сортируем массив для удобства поиска
    sorted_arr = sorted(arr)
    dmin = abs(sorted_arr[1] - sorted_arr[0])

    # Ищем минимальную разность среди соседних элементов
    for i in range(1, n - 1):
        diff = abs(sorted_arr[i + 1] - sorted_arr[i])
        if diff < dmin:
            dmin = diff

    return dmin


if __name__ == "__main__":
    my_array = [10.5, 2.0, 15.1, 7.3, 22.8]

    result = find_min_difference(my_array)
    print(f"Минимальная разность dmin: {result}")