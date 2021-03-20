class Solution:
    def BinarySearch(arr, item):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = arr[mid]

            if guess == item:
                return mid
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    arr = [1, 3, 5, 6, 7, 8]
    print(BinarySearch(arr, 3))
    print(BinarySearch(arr, -1))
