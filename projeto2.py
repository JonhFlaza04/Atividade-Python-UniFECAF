class Cpf:
    def __init__(self, main_string):
        self.main_string = main_string
        self.validate_main_string()

        self.first_digits = []
        for index in range(0, 9):
            self.first_digits.append(int(main_string[index]))

        self.first_verifier_digit = int(main_string[9])
        self.second_verifier_digit = int(main_string[10])

    def invalid(self, message):
        print(f"O CPF {self.main_string} falhou no processo de validação")
        print(f"Erro: {message}")
        exit(0)

    def validate_main_string(self):
        if not self.main_string.isdigit():
            self.invalid("O CPF deve conter apenas números")
        if not len(self.main_string) == 11:
            self.invalid("O CPF deve conter exatamente 11 dígitos")

    def validate_first_verifier_digit(self):
        digits = []
        digits.extend(self.first_digits)

        accumulator = 0
        multiplier = 10
        for digit in digits:
            accumulator += digit * multiplier
            multiplier -= 1

        modulo = (accumulator * 10) % 11
        if modulo == 10:
            modulo = 0

        if not modulo == self.first_verifier_digit:
            self.invalid("A validação do primeiro dígito verificador do CPF falhou")

    def validate_second_verifier_digit(self):
        digits = []
        digits.extend(self.first_digits)
        digits.append(self.first_verifier_digit)

        accumulator = 0
        multiplier = 11
        for digit in digits:
            accumulator += digit * multiplier
            multiplier -= 1

        modulo = (accumulator * 10) % 11
        if modulo == 10:
            modulo = 0

        if not modulo == self.second_verifier_digit:
            self.invalid("A validação do segundo dígito verificador do CPF falhou")


if __name__ == "__main__":
    while True:
        cpf_main_string = input("Por favor, informe o CPF (somente números): ")

        cpf = Cpf(cpf_main_string)
        cpf.validate_first_verifier_digit()
        cpf.validate_second_verifier_digit()

        print(f"O CPF {cpf.main_string} passou na validação")

        should_continue = input("Gostaria de continuar? [y/n]: ")
        if not should_continue.lower() == "y":
            print("Até mais!")
            exit(0)