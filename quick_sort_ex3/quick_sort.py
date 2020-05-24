import random
import numpy as np


def QuickSort(array: list):
    """This QuickSort function runs the recursive quick sort algorithm 
    on an input list

    Arguments:
        array {list} -- The input array

    Returns:
        sorted_array -- A sorted version of the input array
    """
    n = len(array)
    if n > 1:
        array, pivot_initial_index = ChoosePivot(array[:], n)

        array, pivot_final_index = Partition(array[:])
        # print(array)
        sorted_first = QuickSort(array[:pivot_final_index])
        sorted_second = QuickSort(array[(pivot_final_index + 1):])

        sorted_array = sorted_first + [array[pivot_final_index]] + sorted_second
    else:
        sorted_array = array
    
    return sorted_array

def ChoosePivot(array, n: int):
    """The ChoosePivot function chooses a pivot using a median 
    approach from the input array of length n and swaps the pivot 
    to the first element

    Arguments:
        n {int} -- The length of the input array

    Returns:
        array {list} -- The array with the pivot in the first element
        pivot_index {int} -- The index of the pivot element in the original array
    """
    if n % 2:
        mid_idx = int(n / 2)
    else:
        mid_idx = int(n / 2) - 1

    pivot_index = np.where(array == np.median([array[0], array[-1], array[mid_idx]]))[0][0]

    array[0], array[pivot_index] = array[pivot_index], array[0]

    return array, pivot_index

def Partition(array: list):
    """The Partition function partitions an array around a pivot 
    (which is stored as the first element of the array), where all 
    elements before the pivot are smaller and all after are greater

    Arguments:
        array {list} -- The input array

    Returns:
        array {list} -- The partitioned array
        pivot_final_index {list} -- The final index of the pivot after partitioning
    """

    pivot = array[0]
    i = 1
    for j in range(1, len(array)):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1

    pivot_final_index = i - 1
    array[0], array[pivot_final_index] = array[pivot_final_index], array[0]

    return array, pivot_final_index


if __name__=="__main__":
    with open('QuickSort.txt', 'r') as f:
        unsorted_array = f.readlines()
    unsorted_array = [int(val.replace('\n', '')) for val in unsorted_array]
    sorted_array = QuickSort(unsorted_array)
    print(f"Sorted correctly: {sorted_array == sorted(unsorted_array)}")
