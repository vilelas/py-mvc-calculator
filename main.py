from Controller.controller import CalculatorController
from Model.model import CalculatorModel
from View.view import CalculatorView


# main
def main():
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)

    while True:
        view.display_menu()
        operator = view.get_operator()
        
        if operator == 0:
            break
        
        if not controller.validate_operator(operator):
            view.display_error("Opção inválida")
            continue
        
        try:
            result = controller.perform_operation(operator)
        except Exception as e:
            view.display_error(str(e))

if __name__ == "__main__":
    main()
