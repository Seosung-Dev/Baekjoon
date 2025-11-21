def main():
    A, B, V = map(int, input().split())
    move = 0 #날짜
    X = 0 #올라간 거리
    while True:
        X += A
        move += 1
        if X == V: #마지막 날에는 미끄러지지 않는다 : X -= B 하기전에 조건문을 넣어 다 올라갔는지 확인한디.
            break
        else: X -= B
    print(move)
    return 0
if __name__ == "__main__":
    main()