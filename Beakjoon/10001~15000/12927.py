def main():
    lights = list(input().strip()) #전구의 상태를 입력받아 리스트로 변환합니다.
    sum = 0 #스위치를 몇 번 눌러야 하는지 출력하기 위한 변수.
    for i in range(len(lights)):
        if lights[i] == "Y":
            for j in range(i, len(lights), i+1):
                if lights[j] == "Y":
                    lights[j] = "N"
                else:
                    lights[j] = "Y"
            sum+=1
    print(sum)
    return 0
if __name__ == "__main__":
    main()