def main():
    t = int(input())  # 테스트 케이스 개수
    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())  # 행성계 수
        count = 0
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            inside_start = (x1 - cx)**2 + (y1 - cy)**2 < r**2
            inside_end   = (x2 - cx)**2 + (y2 - cy)**2 < r**2
            if inside_start != inside_end:
                count += 1
        print(count)

if __name__ == "__main__":
    main()
