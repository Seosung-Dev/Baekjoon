def main():
    alphabets = list(input())
    answer = len(alphabets)

    for i in range(0, len(alphabets)-2, 1):
        if alphabets[i] == "d" and alphabets[i+1] == "z" and alphabets[i+2] == "=":
            answer -= 1

    for j in range(0, len(alphabets)-1, 1):
        if alphabets[j] == "c" and alphabets[j+1] == "=":
            answer -= 1

        elif alphabets[j] == "c" and alphabets[j+1] == "-":
            answer -= 1

        elif alphabets[j] == "d" and alphabets[j+1] == "-":
            answer -= 1

        elif alphabets[j] == "l" and alphabets[j+1] == "j":
            answer -= 1

        elif alphabets[j] == "n" and alphabets[j+1] == "j":
            answer -= 1

        elif alphabets[j] == "z" and alphabets[j+1] == "=":
            answer -= 1

        elif alphabets[j] == "s" and alphabets[j+1] == "=":
            answer -= 1
    
    print(answer)
    return 0
if __name__ == "__main__":
    main()