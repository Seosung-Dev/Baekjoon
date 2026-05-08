def main():
    N = int(input())
    A = N//10
    B = N%10
    lists = [0, 0, 0, 0, 0, 0]
    finish = [A, B, 5, 9, 5, 9]
    total = 0
    while True:
        lists[5] += 1
        if lists[5] == 10:
            lists[5] = 0
            lists[4] += 1
        if lists[4] == 6:
            lists[4] = 0
            lists[3] += 1  
        if lists[3] == 10:
            lists[3] = 0
            lists[2] += 1
        if lists[2] == 6:
            lists[2] = 0
            lists[1] += 1
        if lists[1] == 10:
            lists[1] = 0
            lists[0] += 1
        
        if 5 in lists:
            total += 1
        if lists == finish:
            break
    print(total)
    return 0
if __name__ == "__main__":
    main()