def MergeSort(array, N):
    """This implementation of the merge sort routine sorts and array of length N

    Arguments:
        array {list} -- The input array to be sorted
        N {int} -- The length of the inputted array

    Returns:
        list -- The sorted array
    """
    if N == 1:
        return array
    else:
        Nx = N // 2
        Ny = int(np.ceil(N / 2))

        A = MergeSort(array[:Nx], Nx)
        B = MergeSort(array[Nx:], Ny)
        sorted_array = Merge(A, B, N)

        return sorted_array

def Merge(A, B, N):
    """This subroutine merges and sorts two sorted input arrays

    Arguments:
        A {list} -- The first sorted array
        B {list} -- The second sorted array
        N {int} -- The total length of the A and B

    Returns:
        list -- The merged sorted array of the two input sorted arrays
    """
    i = 0
    j = 0
    C = [0]*N

    for k in range(N):
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        elif A[i] > B[j]:
            C[k] = B[j]
            j += 1

        if i >= len(A):
            C[(k + 1):] = B[j:]
            break
        elif j >= len(B):
            C[(k + 1):] = A[i:]
            break
    
    return C
