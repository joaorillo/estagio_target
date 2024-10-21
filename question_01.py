def main():
    while True:
        user_input = input("Informe um número: ")
        try:
            number = int(user_input)
            if str(number) == user_input:
                break
        except ValueError:
            pass
        print("Entrada inválida.\n")
    last_two = [0, 1]
    while last_two[1] <= number or number == 0:
        if number in last_two:
            print(f"{number} pertence à sequência de Fibonacci.")
            return
        last_two = [last_two[1], last_two[0] + last_two[1]]
    print(f"{number} não pertence à sequência de Fibonacci.")
    return


if __name__ == "__main__":
    main()
    