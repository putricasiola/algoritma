# Pseudocode Merge Sort
# function mergeSort(arr):
#     if length(arr) <= 1:
#         return arr
#     mid = length(arr) // 2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])
#     return merge(left, right)

# function merge(left, right):
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result + left + right

# Analisis Kompleksitas:

# Best Case (Big Θ): 
# 𝑂(𝑛log⁡𝑛) O(nlogn)
# Karena meskipun data sudah terurut, merge sort tetap membagi array hingga level terkecil dan melakukan penggabungan.
# Worst Case (Big O): 
# 𝑂(𝑛log⁡𝑛) O(nlogn)
# Semua data dipecah dan digabung dengan perbandingan di setiap level rekursi.
# Space Complexity: 
# 𝑂(𝑛) O(n) karena array baru dibuat di setiap proses penggabungan.

#Pseudocode Bubble Sort
# function bubbleSort(arr):
#     n = length(arr)
#     for i from 0 to n-1:
#         for j from 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                 swap(arr[j], arr[j+1])

# Analisis Kompleksitas:

# Best Case (Big Θ): 
# 𝑂(𝑛) Jika data sudah terurut, algoritma hanya melakukan satu iterasi dan tidak ada pertukaran.
# Worst Case (Big O): 
# 𝑂(𝑛2)
# Jika data terbalik urutannya, algoritma melakukan perbandingan maksimum di setiap iterasi.
# Space Complexity: 
# O(1), karena sorting dilakukan secara in-place.

#Kode Program
import random
import time

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Generate 100 random integers
arr = [random.randint(1, 1000) for _ in range(100)]

# Merge Sort Execution
merge_arr = arr.copy()
start_time = time.time()
merge_sorted = merge_sort(merge_arr)
merge_time = time.time() - start_time

# Bubble Sort Execution
bubble_arr = arr.copy()
start_time = time.time()
bubble_sorted = bubble_sort(bubble_arr)
bubble_time = time.time() - start_time

# Print Results
print("Original Array:", arr)
print("\nMerge Sort Result:", merge_sorted)
print(f"Merge Sort Time: {merge_time:.6f} seconds")
print("\nBubble Sort Result:", bubble_sorted)
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")

