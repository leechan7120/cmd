"""View 계층 (완성본 - 수정하지 않아도 됩니다)

tkinter 로 만든 계산기 화면입니다.
- 화면 그리기와 사용자 입력 '전달'만 담당하고, 계산은 전혀 하지 않습니다.
- 버튼을 클릭하거나 키보드를 누르면 등록된 핸들러를 key 문자열과 함께 호출합니다.

핸들러로 전달되는 key 값:
    "0"~"9", ".", "+", "-", "×", "÷", "=", "C", "⌫", "±"

Controller 가 사용하는 공개 메서드:
    set_key_handler(handler)  : 키 입력 시 호출될 함수 등록 (handler(key: str) -> None)
    set_display(text)         : 메인 화면 텍스트 변경
    set_expression(text)      : 위쪽 작은 수식 텍스트 변경
    run()                     : 창 띄우기 (mainloop)
"""

import tkinter as tk
from typing import Callable, Optional

KeyHandler = Callable[[str], None]

# 색상 테마
BG = "#1c1c1e"
FG = "#ffffff"
SUB_FG = "#8e8e93"
COLOR_DIGIT = ("#333336", "#4a4a4e")      # (기본, 마우스 올렸을 때)
COLOR_FUNC = ("#5a5a5f", "#76767c")
COLOR_OP = ("#ff9f0a", "#ffb340")

BUTTON_LAYOUT = [
    [("C", 1), ("⌫", 1), ("±", 1), ("÷", 1)],
    [("7", 1), ("8", 1), ("9", 1), ("×", 1)],
    [("4", 1), ("5", 1), ("6", 1), ("-", 1)],
    [("1", 1), ("2", 1), ("3", 1), ("+", 1)],
    [("0", 2), (".", 1), ("=", 1)],
]

OPERATOR_KEYS = {"÷", "×", "-", "+", "="}
FUNCTION_KEYS = {"C", "⌫", "±"}

KEYSYM_MAP = {
    "Return": "=",
    "KP_Enter": "=",
    "BackSpace": "⌫",
    "Escape": "C",
}
CHAR_MAP = {
    "*": "×",
    "/": "÷",
    "x": "×",
}
VALID_CHARS = set("0123456789.+-=")


class CalculatorView(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.configure(bg=BG)
        self.resizable(False, False)

        self._key_handler: Optional[KeyHandler] = None
        self._display_var = tk.StringVar(value="0")
        self._expression_var = tk.StringVar(value="")

        self._create_display()
        self._create_keypad()
        self.bind("<Key>", self._on_keyboard)

    def set_key_handler(self, handler: KeyHandler) -> None:
        self._key_handler = handler

    def set_display(self, text: str) -> None:
        self._display_var.set(text)
        size = 40 if len(text) <= 9 else 30 if len(text) <= 12 else 22
        self._display_label.configure(font=("Helvetica", size))

    def set_expression(self, text: str) -> None:
        self._expression_var.set(text)

    def run(self) -> None:
        self.mainloop()

    def _create_display(self) -> None:
        frame = tk.Frame(self, bg=BG)
        frame.pack(fill="x", padx=14, pady=(18, 8))

        tk.Label(
            frame, textvariable=self._expression_var, anchor="e",
            bg=BG, fg=SUB_FG, font=("Helvetica", 14), height=1,
        ).pack(fill="x")

        self._display_label = tk.Label(
            frame, textvariable=self._display_var, anchor="e",
            bg=BG, fg=FG, font=("Helvetica", 40), width=12,
        )
        self._display_label.pack(fill="x")

    def _create_keypad(self) -> None:
        keypad = tk.Frame(self, bg=BG)
        keypad.pack(padx=10, pady=(0, 14))

        for row_index, row in enumerate(BUTTON_LAYOUT):
            col = 0
            for key, span in row:
                self._create_button(keypad, key, row_index, col, span)
                col += span

        for col in range(4):
            keypad.columnconfigure(col, weight=1, uniform="key")

    def _create_button(self, parent: tk.Frame, key: str, row: int, col: int, span: int) -> None:
        if key in OPERATOR_KEYS:
            normal, hover = COLOR_OP
        elif key in FUNCTION_KEYS:
            normal, hover = COLOR_FUNC
        else:
            normal, hover = COLOR_DIGIT

        button = tk.Label(
            parent, text=key, bg=normal, fg=FG,
            font=("Helvetica", 20), width=4, cursor="hand2",
        )
        button.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=4, pady=4, ipady=12)

        button.bind("<Button-1>", lambda _e, k=key: self._press(k))
        button.bind("<Enter>", lambda _e, b=button, c=hover: b.configure(bg=c))
        button.bind("<Leave>", lambda _e, b=button, c=normal: b.configure(bg=c))


    def _press(self, key: str) -> None:
        if self._key_handler is not None:
            self._key_handler(key)

    def _on_keyboard(self, event: tk.Event) -> None:
        if event.keysym in KEYSYM_MAP:
            self._press(KEYSYM_MAP[event.keysym])
        elif event.char in CHAR_MAP:
            self._press(CHAR_MAP[event.char])
        elif event.char and event.char in VALID_CHARS:
            self._press(event.char)