def main():
    N = int(input())
    for i in range(2, N-1, 1):
        if N % i == 0:
            print("No")
            return 0
    print("Yes")
    return 0
if __name__ == "__main__":
    main()