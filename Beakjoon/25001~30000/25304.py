def main():
    X = int(input())
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += A*B
    if X == sum:
        print("Yes")
    else:
        print("No")
    return 0
if __name__ == "__main__":
    main()