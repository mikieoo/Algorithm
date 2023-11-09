def partition(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[low], arr[right] = arr[right], arr[low]

    return right


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


file_path = "input_quick_sort"
with open(file_path, 'r') as file:
    lines = file.readlines()

arr = [int(line.strip()) for line in lines]

n = len(arr)
quick_sort(arr, 0, n - 1)

output_file_path = "output_quick_sort"
with open(output_file_path, 'w') as file:
    for num in arr:
        file.write(str(num) + '\n')

print("퀵 정렬 결과를", output_file_path, "에 저장했습니다.")
