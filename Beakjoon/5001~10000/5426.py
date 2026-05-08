import math

def main():
    T = int(input())
    A = []
    for _ in range(T):
        x = 0
        letters = list(input().strip())
        for_cal = []
        answer = []
        square = int(math.sqrt(len(letters)))
        for a in range(square):
            cal = []
            for b in range(square):
                cal.append(letters[b+x])
            for_cal.append(cal)
            x += square
        for i in range(square-1, -1, -1):
            for j in range(0, square, 1):
                answer.append(for_cal[j][i])
        A.append("".join(answer))
    for w in A:
        print(w)
    return 0
if __name__ == "__main__":
    main()