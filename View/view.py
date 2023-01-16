# View
class CalculatorView:
    def display_menu(self):
        self.choice = {
            1: "Soma",
            2: "Subtração",
            3: "Multiplicação",
            4: "Divisão",
            0: "Sair"
        }

        for k, v in self.choice.items():
            print(f"[{k}] - {v}")
    
    def get_input(self):
        x = input("1º número: ")
        y = input("2º número: ")
        return (x, y)

    def get_operator(self):
        operator = int(input("Escolha a operação: "))
        return operator
    
    def display_result(self, result):
        print(f"Resultado: {result}")

    def display_error(self, e):
        print(e)
