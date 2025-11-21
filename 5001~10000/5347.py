import math

def main():
    N = int(input())
    answer = []
    for _ in range(N):
        a,b = map(int, input().split())
        answer.append(math.lcm(a, b))
    for i in answer:
        print(i)
    return 0
if __name__ == "__main__":
    main()