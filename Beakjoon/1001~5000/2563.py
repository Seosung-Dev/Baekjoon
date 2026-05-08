def main():
    count = int(input())
    CoordinatePlane = [[0 for _ in range(100)] for _ in range(100)]

    if count > 100:
        print("error")
    
    for _ in range(count):
        x, y = map(int, input().split())
        for i in range(x, x+10, 1):
            for j in range(y, y+10, 1):
                CoordinatePlane[i][j] = 1
    
    answer = 0

    for a in range(100):
        for b in range(100):
            answer += CoordinatePlane[a][b]

    print(answer)
       
    return 0
if __name__ == "__main__":
    main()