from numpy import ceil, floor
import time

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

def katsuba(x, y):
    x_str = str(x)
    y_str = str(y)
    Nx = len(x_str)
    Ny = len(y_str)

    N_diff = abs(Nx - Ny)

    if N_diff == 0:
        N = Nx

    elif Nx > Ny:
        N = Nx
        y_str = str(y * 10**N_diff)

    elif Ny > Nx:
        N = Ny
        x_str = str(x * 10**N_diff)
    
    else: 
        print('ERROR')
        exit()

    if N > 1:
        print(x_str, y_str)
        a = int(x_str[:int(ceil(N / 2))])
        b = int(x_str[int(floor(N / 2)):])
        c = int(y_str[:int(ceil(N / 2))])
        d = int(y_str[int(floor(N / 2)):])

        print(f"a: {a}, b: {b}, c: {c}, d: {d}")

        ac = katsuba(a, c)
        bd = katsuba(b, d)
        brac_prod = katsuba(a + b, c + d)
        gauss_term = brac_prod - ac - bd
        
        product = 10**N * ac + 10**(N / 2) * (gauss_term) + bd

        product = product / 10**N_diff
    else:
        product = x * y

    return int(product)

# start = time.time()
# result = katsuba(num1, num2)
# duration = time.time() - start
# print(result)
# print(f'Katsuba took: {duration}')

start = time.time()
inbuilt_product = num1 * num2
duration = time.time() - start
print(inbuilt_product)
# assert(result == inbuilt_product)

print(f'Python took: {duration}')
