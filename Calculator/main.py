"""실행 방법:
    python main.py
"""

from controller.CalculatorController import CalculatorController
from domain.Calculator import Calculator
from view.CalculatorView import CalculatorView


def main() -> None:
    model = Calculator()
    view = CalculatorView()
    CalculatorController(model, view)
    view.run()


if __name__ == "__main__":
    main()