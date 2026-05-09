import math

N = int(input())
dots = []
answer = 99999
for a in range(N):
    x, y = 0, 0
    x, y = map(int, input().split())
    dots.append([x, y])

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a, b, c = 0, 0, 0
            a = (dots[j][0] - dots[i][0]) ** 2 + (dots[j][1] - dots[i][1]) ** 2
            b = (dots[k][0] - dots[j][0]) ** 2 + (dots[k][1] - dots[j][1]) ** 2
            c = (dots[k][0] - dots[i][0]) ** 2 + (dots[k][1] - dots[i][1]) ** 2

            print(a, b, c)
            if a == b:
                if a + b == c:
                    if c < answer:
                        answer = c
            if b == c:
                if b + c == a:
                    if a < answer:
                        answer = a
            if c == a:
                if c + a == b:
                    if b < answer:
                        answer = b

print(int(math.sqrt(answer)))