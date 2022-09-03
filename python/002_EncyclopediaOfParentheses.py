
def main(N):
    S = '('
    T = ')'

    # Enumerate all combinations in the list
    for i in range(2 ** N):
        # Convert the number to binary
        s = format(i, 'b').zfill(N)
        # Replace 0 with '(' and 1 with ')'
        s = s.replace('0', S).replace('1', T)
        # Check if the parentheses are balanced
        if is_ok(s):
            print(s)

def is_ok(s):
    # Check if the parentheses are balanced
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    return count == 0

if __name__ == '__main__':
    # Input one variable N
    N = int(input())

    # main 
    main(N)
