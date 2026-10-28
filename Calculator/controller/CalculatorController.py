"""Controller 계층

View 에서 들어온 입력(key)을 해석해서 Model(Calculator)을 호출하고,
그 결과를 다시 View 에 반영하는 '중간 다리' 역할을 합니다.
- 계산 규칙은 Model 이 담당합니다. (Controller 에 계산 로직을 넣지 마세요)
- 화면 그리기는 View 가 담당합니다. (Controller 에서 tkinter 를 직접 다루지 마세요)

View 가 넘겨주는 key 값:
    "0"~"9", ".", "+", "-", "×", "÷", "=", "C", "⌫", "±"

View 가 제공하는 메서드:
    view.set_display(text)
    view.set_expression(text)
"""

from domain.Calculator import Calculator
from view.CalculatorView import CalculatorView


class CalculatorController:
    def __init__(self, model: Calculator, view: CalculatorView) -> None:
        self.model = model
        self.view = view

        # View 에서 키가 눌리면 handle_key 가 호출되도록 연결합니다.
        self.view.set_key_handler(self.handle_key)

    def handle_key(self, key: str) -> None:
        """View 에서 들어온 key 에 맞는 Model 메서드를 호출합니다."""
        # TODO: key 종류에 따라 model 의 메서드를 호출하세요.
        #   숫자 -> model.input_digit(key)
        #   "."  -> model.input_decimal_point()
        #   연산자 -> model.input_operator(key)
        #   ...
        # 마지막에는 update_view() 로 화면을 갱신하세요.
        pass

    def update_view(self) -> None:
        """Model 의 현재 상태를 View 에 반영합니다."""
        # TODO: self.view.set_display(...), self.view.set_expression(...) 호출
        pass