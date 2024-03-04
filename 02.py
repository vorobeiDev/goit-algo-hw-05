def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = None
    return iterations, upper_bound


if __name__ == '__main__':
    sorted_array = [2.33, 3.44, 5.55, 6.66, 7, 8.88, 9.99, 10.10, 11.11, 12, 13.13, 14.14, 15.15, 16.16, 17.17, 18, 19.19, 20.20, 21]
    print(binary_search(sorted_array, 7))
