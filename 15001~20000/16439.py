def main():
    N,M=map(int,input().split())
    total=0
    members=[list(map(int,input().split())) for _ in range(N)]
    for i in range(M):
        for j in range(i+1,M):
            for k in range(j+1,M):
                cal=0
                for list_1 in members:
                    cal+=max(list_1[i],list_1[j],list_1[k])
                if cal>total:
                    total=cal
    print(total)
    return 0
if __name__=="__main__":
    main()