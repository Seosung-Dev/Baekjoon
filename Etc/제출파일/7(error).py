def main():
    N = int(input())
    dic = []
    lists = []
    listss = [] #임시
    total = 0
    answer = []
    for _ in range(N):
        a, b = map(int, input().split())
        listss = [a, b]
        dic.append(listss)
    for i in range(len(dic)):
        x = dic[i][0]
        for j in range(len(dic)):
            for g in range(2):
                if x <= dic[0][g]:
                    lists.append(dic[0][g])
                    total += 1
            x = min(lists)
            answer.append(total)
    print(min(answer))
    return 0
if __name__ == "__main__":
    main()