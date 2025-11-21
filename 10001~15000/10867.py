def main():
    N = int(input())
    num_list = set(map(int, input().split()))
    num_list = sorted(list(num_list))
    for i in num_list:
        print(i)
    return 0
if __name__ == "__main__":
    main()