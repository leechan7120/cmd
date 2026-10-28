"""Domain(Model) 계층

계산기의 '상태'와 '계산 규칙'만 담당합니다.
- tkinter 등 UI 관련 코드는 절대 import 하지 않습니다.
- 화면에 어떻게 보일지는 모릅니다. 문자열(display)만 돌려줍니다.

지원해야 하는 입력(View 에서 넘어오는 키):
    숫자      : "0" ~ "9"
    소수점    : "."
    연산자    : "+", "-", "×", "÷"
    계산      : "="
    초기화    : "C"
    한 글자 삭제 : "⌫"
    부호 전환 : "±"

구현 시 고민해 볼 것:
    - 연산자를 연속으로 누르면? (예: 5 + × 3)
    - "=" 를 누른 뒤 숫자를 누르면 새 계산? 이어서 계산?
    - 0 으로 나누면? (예: ZeroDivisionError 를 발생시킬지, 에러 상태로 둘지)
    - 소수점을 두 번 누르면? "007" 처럼 앞자리 0 은?
    - 결과가 정수일 때 "3.0" 이 아니라 "3" 으로 보여줄지?
"""


class Calculator:
    """계산기의 상태를 가지고 계산을 수행하는 도메인 객체."""

    def __init__(self) -> None:
        # TODO: 계산에 필요한 상태를 정의하세요.
        #   예) 현재 입력 중인 값, 저장된 이전 값, 선택된 연산자, 에러 여부 ...
        pass

    def input_digit(self, digit: str) -> None:
        """숫자("0"~"9")를 현재 입력값 뒤에 이어 붙입니다."""
        # TODO
        raise NotImplementedError

    def input_decimal_point(self) -> None:
        """소수점을 입력합니다. (이미 있으면 무시하는 등의 규칙을 정하세요)"""
        # TODO
        raise NotImplementedError

    def input_operator(self, operator: str) -> None:
        """연산자("+", "-", "×", "÷")를 선택합니다."""
        # TODO
        raise NotImplementedError

    def toggle_sign(self) -> None:
        """현재 값의 부호(+/-)를 바꿉니다."""
        # TODO
        raise NotImplementedError

    def delete_last(self) -> None:
        """현재 입력값의 마지막 한 글자를 지웁니다."""
        # TODO
        raise NotImplementedError

    def clear(self) -> None:
        """모든 상태를 초기화합니다."""
        # TODO
        raise NotImplementedError

    def calculate(self) -> None:
        """저장된 값, 연산자, 현재 값으로 결과를 계산합니다."""
        # TODO
        raise NotImplementedError

    def get_display(self) -> str:
        """메인 화면에 보여줄 문자열을 반환합니다. (예: "0", "12.5", "Error")"""
        # TODO
        raise NotImplementedError

    def get_expression(self) -> str:
        """작은 글씨로 보여줄 수식 문자열을 반환합니다. (예: "12 +") 없으면 빈 문자열"""
        # TODO
        raise NotImplementedError