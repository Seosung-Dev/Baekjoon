def main():
    answer = []
    T = int(input())
    for _ in range(T):
        lists = []
        lists = input().strip()
        A = [0]
        B = [0]
        a = 0
        b = 0
        seeing = 0
        for i in lists:
            if i == "F":
                if seeing == 0:
                    a += 1
                    A.append(a)
                elif seeing == 1:
                    b += 1
                    B.append(b)
                elif seeing == 2:
                    a -= 1
                    A.append(a)
                elif seeing == 3:
                    b -= 1
                    B.append(b)
            elif i == "B":
                if seeing == 0:
                    a -= 1
                    A.append(a)
                elif seeing == 1:
                    b -= 1
                    B.append(b)
                elif seeing == 2:
                    a += 1
                    A.append(a)
                elif seeing == 3:
                    b += 1
                    B.append(b)
            elif i == "L":
                seeing = (seeing - 1) % 4
            elif i == "R":
                seeing = (seeing + 1) % 4
        As = min(A)
        Al = max(A)
        Bs = min(B)
        Bl = max(B)
        if As < 0 and Bs < 0:
            answer.append((Al-As)*(Bl-Bs))
        elif As < 0:
            answer.append((Al-As)*(Bl))
        elif Bs < 0:
            answer.append((Al)*(Bl-Bs))
        else:
            answer.append(Al*Bl)
    for j in answer:
        print(j)
    return 0
if __name__ == "__main__":
    main()