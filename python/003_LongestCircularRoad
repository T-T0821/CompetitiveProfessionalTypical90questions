
def dfs(tree, i, parent):
    # Calculate the longest path from node i
    longest = 0
    for j in tree[i]:
        if j != parent:
            longest = max(longest, dfs(tree, j, i))

    return longest + 1

if __name__ == '__main__':
    # Input one variable N
    N = int(input())

    # Input 2 variable's N-1 times
    A = [list(map(int, input().split())) for _ in range(N - 1)]

    # Step #2. Find the shortest distance from vertex 1
    # maxid1: The vertex farthest (longest shortest distance) from vertex 1
    # maxd1: The longest shortest distance from vertex 1
    maxid1 = 0
    maxd1 = 0
    for i in range(N):
        # Step #1. Construct a tree
        tree = [[] for _ in range(N + 1)]
        for a in A:
            tree[a[0]].append(a[1])
            tree[a[1]].append(a[0])

        # Step #2. Find the shortest distance from vertex 1
        d = dfs(tree, i + 1, -1)
        if d > maxd1:
            maxid1 = i + 1
            maxd1 = d

    # Print the answer
    print(maxd1)