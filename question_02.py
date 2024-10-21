def main():
    user_input = input("Informe uma string: ")
    count = 0
    for character in user_input:
        if character.lower() == 'a':
            count += 1
    print(f"{count} aparições da letra 'a'")


if __name__ == "__main__":
    main()
    