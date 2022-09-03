if __name__ == '__main__':
    # Input one variable N W
    N, W = map(int, input().split())
    # Input n variable's N * W
    A = [list(map(int, input().split())) for _ in range(N)]
    # Outputs the sum of the elements in the same row and column of a matrix Cython
    for i in range(N):
        for j in range(W):
            print(sum(A[i]) + sum([A[k][j] for k in range(N)]) - A[i][j], end=' ')
        print()