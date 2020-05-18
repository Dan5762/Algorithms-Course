import numpy as np

def Count(array, N):
    """This routine counts the number of split inversions in a list, it also returns the sorted list

    Arguments:
        array {list} -- The input array
        N {int} -- The length of the inputted array

    Returns:
        d {list} -- The sorted array
        split_inv_count {int} -- The total number of split inversions
    """
    if N == 1:
        return array, 0
    else:
        Nx = N // 2
        Ny = int(np.ceil(N / 2))

        b, x = Count(array[:Nx], Nx)
        c, y = Count(array[Nx:], Ny)
        d, z = MergeCountSplitInv(b, c, N)
        
        split_inv_count = x + y + z

        return d, split_inv_count

def MergeCountSplitInv(A, B, N):
    """This subroutine merges and sorts two sorted input arrays, it also records the number of split inversions.

    Arguments:
        A {list} -- The first sorted array
        B {list} -- The second sorted array
        N {int} -- The total length of the A and B

    Returns:
        C {list} -- The merged sorted array of the two input sorted arrays
        n_split_inv {list} -- The number of split inversions in the two input arrays
    """
    i = 0
    j = 0
    C = [0]*N
    n_split_inv = 0

    for k in range(N):
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        elif A[i] > B[j]:
            C[k] = B[j]
            j += 1
            n_split_inv += len(A[i:])

        if i >= len(A):
            C[(k + 1):] = B[j:]
            break
        elif j >= len(B):
            C[(k + 1):] = A[i:]
            break
    
    return C, n_split_inv

if __name__=="__main__":
    array = []
    with open("IntegerArray.txt") as f:
        for number in f:
            array.append(int(number.split('/')[0]))
    sorted_array, n_split_inv = Count(array, len(array))
    print(n_split_inv)