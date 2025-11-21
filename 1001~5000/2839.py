def main():
    N = int(input())
    count = 0
    while N >= 0:
        if N % 5 == 0:
            count += N // 5
            print(count)
            return
        N -= 3
        count += 1
    print(-1)
if __name__ == "__main__":
    main()
