def fibonacci_count(n):
    zero = [1, 0]
    one = [0, 1]

    for i in range(2, n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])

    return zero[n], one[n]

def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        z, o = fibonacci_count(x)
        print(z, o)

if __name__ == "__main__":
    main()
