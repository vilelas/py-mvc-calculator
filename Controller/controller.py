# Controller
class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def perform_operation(self, operator):
        x, y = self.view.get_input()

        try:
            x, y = float(x), float(y)
        except Exception as e:
            self.view.display_error(e)
     
        if operator == 1:
            result = self.model.add(x, y)
        elif operator == 2:
            result = self.model.subtract(x, y)
        elif operator == 3:
            result = self.model.multiply(x, y)
        elif operator == 4:
            result = self.model.divide(x, y)

        self.view.display_result(result)

    def validate_operator(self, operator):
        if operator not in list(self.view.choice.keys()):
            return False
        return True