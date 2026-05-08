def main():
    N = int(input())
    x = []
    total = 0
    cal = 0
    for _ in range(N):
        a = list(map(int, input().split()))
        y = 0
        for k in range(1, len(a), 1):
            y += a[k]
        x.append(y)
        y = 0
    x.sort()
    for i in x:
        total += (i + cal)
        cal += i
    print(total)
if __name__ == "__main__":
    main()