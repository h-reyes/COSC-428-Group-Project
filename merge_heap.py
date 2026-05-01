# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:11:45 2026

@author: recre
"""

import random
import time


# Merge Sort
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# Small test
arr = [38, 27, 43, 3, 9, 82, 10]

print("Original:", arr)
print("Merge Sort:", merge_sort(arr.copy()))
print("Heap Sort: ", heap_sort(arr.copy()))

print("\nComplexities:")
print("Merge Sort -> Time: O(n log n), Space: O(n)")
print("Heap Sort  -> Time: O(n log n), Space: O(1)")


# Performance Comparison
def test_algorithms(size):
    arr = [random.randint(1, 10000) for _ in range(size)]

    print("\n==============================")
    print("Input Size:", size)
    print("Random Numbers Chosen:", arr)

    start = time.perf_counter()
    merge_sorted = merge_sort(arr.copy())
    merge_time = time.perf_counter() - start

    start = time.perf_counter()
    heap_sorted = heap_sort(arr.copy())
    heap_time = time.perf_counter() - start

    print("Sorted by Merge Sort:", merge_sorted)
    print("Sorted by Heap Sort: ", heap_sorted)
    print("Merge Sort Time:", round(merge_time * 1000, 2), "ms")
    print("Heap Sort Time: ", round(heap_time * 1000, 2), "ms")

    return merge_time, heap_time


def get_sizes_from_user():
    available_sizes = [10, 100, 1000, 5000, 10000]
    prompt = (
        "Choose sizes from the available options: "
        f"{available_sizes}\n"
        "Enter one or more sizes separated by commas, or press Enter to use all default sizes: "
    )
    user_input = input(prompt).strip()

    if not user_input:
        return available_sizes

    try:
        sizes = [int(part.strip()) for part in user_input.split(",") if part.strip()]
        if not sizes or any(size not in available_sizes for size in sizes):
            raise ValueError
        return sizes
    except ValueError:
        print("Invalid selection. Using default sizes.")
        return available_sizes


sizes = get_sizes_from_user()

for size in sizes:  
    m, h = test_algorithms(size)
    print("\nSummary")
    print("Size | Merge Sort | Heap Sort")
    print("--------------------------------")
    print(size, "|", round(m * 1000, 2), "ms", "|", round(h * 1000, 2), "ms")
