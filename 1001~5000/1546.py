def main():
    T = int(input())
    list_num = list(map(int, input().split()))
    max_list = max(list_num)
    answer = 0
    for i in list_num:
        a = (i/max_list)*100
        answer += a
    print(answer / (T))
if __name__ == "__main__":
    main()
