def main():
    lists = set()

    N = int(input())
    if N > 20000:
        print("error")

    for _ in range(N):
        a = input()
        lists.add(a)

    lists = sorted(lists, key = lambda x: (len(x), x))

    for i in lists:
        print(i)
    
    return 0
if __name__ == "__main__":
    main()