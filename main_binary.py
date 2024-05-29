def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1
 
# 示例使用
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6
index = binary_search(arr, x)
if index != -1:
    print(f"元素 {x} 的索引为 {index}")
else:
    print(f"数组中不存在 {x}")


def insertion_sort(arr):
    for i in range(len(arr)):
        # 获取当前需要排序的元素
        key = arr[i]
        # 从已排序的序列的末尾开始比较，并找到插入点
        j = i - 1
        while j >= 0 and key < arr[j]:
            # 如果发现有元素比当前元素小，则交换它们
            arr[j+1] = arr[j]
            arr[j] = key
            j -= 1
    return arr
 
# 示例使用
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
