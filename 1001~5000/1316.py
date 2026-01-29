def main():
    N = int(input())
    if N > 100:
        print("error")

    answer = 0

    for _ in range(N):
        index = list(input())
        cal = []
        a = index[0]
        x = 0

        for i in index:
            if i == a:
                a = i
                cal.append(i)
            else:
                if i in cal:
                    x = 1
                else:
                    a = i
                    cal.append(i)
        if x != 1:
            answer += 1
    
    print(answer)

    return 0
if __name__ == "__main__":
    main()