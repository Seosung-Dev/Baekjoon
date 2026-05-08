def main():
    a = 0
    total = 0
    N = int(input())
    lists = list(map(int, input().split()))
    for i in lists:
        if i != 1:
            for j in range(2, i-1):
                if i % j == 0 and i != 2:
                    a = 1
                    break
            if a == 0:
                total += 1
            a = 0
    print(total)
    return 0
if __name__ == "__main__":
    main()