def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
 
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Sorted array is:", sorted_array)
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


def find_median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 0:
        # 如果列表长度为偶数，则中位数是中间两个数的平均值
        median1 = n // 2 - 1
        median2 = n // 2
        return (sorted_list[median1] + sorted_list[median2]) / 2
    else:
        # 如果列表长度为奇数，则中位数是中间的单个数
        return sorted_list[n // 2]
 
# 示例
my_list = [1, 3, 5, 7, 9]  # 已排序列表
print(find_median(my_list))  # 输出: 5
