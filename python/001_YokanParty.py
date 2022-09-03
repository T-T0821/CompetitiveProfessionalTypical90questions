import sys

def main(N, L, K, A):
    left = -1
    right = L + 1
    while right - left > 1:
        mid = (left + right) // 2
        if is_ok(N, L, K, A, mid):
            left = mid
        else:
            right = mid

    return left

def is_ok(N, L, K, A, x):
    count = 0
    prev = 0
    for a in A:
        if a - prev >= x and L - a >= x:
            count += 1
            prev = a

    return count >= K

# main
if __name__ == '__main__':
    # Input two variables N, L
    N, L = map(int, input().split())

    # Input one variables K
    K = int(input())

    # Input n variables An
    A = list(map(int, input().split()))

    # Print N, L, K, A
    print(main(N, L, K, A))
