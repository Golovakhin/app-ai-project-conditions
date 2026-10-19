# Контракт Tool (воркшоп 1)
# Имя:        math_condition
# Назначение: Проверяет, удовлетворяет ли число заданному математическому условию.
#             Используй, когда пользователь спрашивает «чётное ли число»,
#             «больше ли нуля», «равно ли X», «в диапазоне ли значение».
# Вход:       value: float — обязателен, любое число
#             condition: str — обязателен, допустимые значения:
#                        'positive', 'negative', 'zero', 'even', 'odd'
# Выход:      JSON-строка; при успехе: {"status": "ok", "value": ..., "condition": ..., "result": true/false}
#             при ошибке: {"status": "error", "message": "<что не так и что делать>"}
# Краевые случаи: неизвестное condition → ошибка с перечислением допустимых;
#                 value не число → ошибка;
#                 нецелое число для 'even'/'odd' → ошибка.ыпш

import json

from crewai.tools import tool


def _fail(message: str) -> str:
    """Единый формат ошибки, который вернётся агенту."""
    return json.dumps({"status": "error", "message": message}, ensure_ascii=False)


@tool("math_condition")
def math_condition(value: float, condition: str) -> str:
    """Проверяет, удовлетворяет ли число заданному математическому условию.

    Args:
        value: число, которое проверяем.
        condition: одно из 'positive', 'negative', 'zero', 'even', 'odd'.

    Returns:
        JSON-строка. При успехе: {"status": "ok", "value": ..., "condition": ..., "result": true/false}.
        При ошибке: {"status": "error", "message": "<что не так и что делать>"}.
    """
    allowed = {"positive", "negative", "zero", "even", "odd"}
    if condition not in allowed:
        return _fail(
            f"condition должен быть одним из {sorted(allowed)}, получено '{condition}'"
        )

    try:
        value = float(value)
    except (TypeError, ValueError):
        return _fail(f"value должен быть числом, получено '{value}'")

    if condition in {"even", "odd"} and not value.is_integer():
        return _fail(f"condition='{condition}' требует целое число, получено {value}")

    if condition == "positive":
        result = value > 0
    elif condition == "negative":
        result = value < 0
    elif condition == "zero":
        result = value == 0
    elif condition == "even":
        result = int(value) % 2 == 0
    else:  # odd
        result = int(value) % 2 != 0

    return json.dumps(
        {"status": "ok", "value": value, "condition": condition, "result": result},
        ensure_ascii=False,
    )