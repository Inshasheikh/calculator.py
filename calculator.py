from __future__ import annotations

import ast
import operator
from datetime import datetime


BANNER = """
╔════════════════════════════════════════════╗
║      ✨ Smart Console Calculator ✨       ║
╠════════════════════════════════════════════╣
║ Use either style:                          ║
║   • Normal mode: number + operator         ║
║   • Quick mode: full expression            ║
║                                            ║
║ Commands: history, clear, help, exit       ║
║ Tip: use 'ans' to reuse previous result    ║
╚════════════════════════════════════════════╝
"""

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    "%": operator.mod,
}

AST_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


class ExpressionError(ValueError):
    """Raised when user enters an invalid expression."""


def calculate_expression(expression: str) -> float:
    """Safely evaluate arithmetic expressions with AST."""
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ExpressionError("Invalid expression syntax.") from exc

    def evaluate(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.BinOp):
            left = evaluate(node.left)
            right = evaluate(node.right)
            op_type = type(node.op)
            if op_type not in AST_OPERATORS:
                raise ExpressionError("Unsupported operator in expression.")
            if op_type is ast.Div and right == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return AST_OPERATORS[op_type](left, right)

        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value

        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)

        raise ExpressionError("Only numbers and arithmetic operators are allowed.")

    return evaluate(tree)


def format_result(result: float) -> str:
    """Display clean integer values without .0"""
    return str(int(result)) if result.is_integer() else f"{result:.10g}"


def get_number(prompt: str, last_result: float) -> float:
    """Read number input and support 'ans' keyword."""
    raw = input(prompt).strip().lower()
    if raw == "ans":
        return last_result
    return float(raw)


def print_help() -> None:
    print("\nHelp:")
    print("- Standard mode: enter a number, operator (+ - * / ^ %), and another number")
    print("- Quick mode: type expression directly, e.g. (12+3)*2/5")
    print("- Commands: history, clear, help, exit")
    print("- Use 'ans' in place of a number to use previous result")


def main() -> None:
    print(BANNER)
    history: list[str] = []
    last_result = 0.0

    while True:
        action = input("\nMode [normal/quick/help/history/clear/exit]: ").strip().lower()

        if action in {"exit", "quit", "q"}:
            print("\nThanks for using Smart Calculator. 👋")
            break

        if action in {"help", "h"}:
            print_help()
            continue

        if action == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("\nRecent calculations:")
                for item in history[-10:]:
                    print(item)
            continue

        if action == "clear":
            history.clear()
            last_result = 0.0
            print("Calculator memory cleared.")
            continue

        try:
            if action in {"quick", "qk"}:
                expression = input("Enter expression: ").strip().lower().replace("ans", str(last_result))
                result = calculate_expression(expression)
                statement = f"{expression} = {format_result(result)}"

            elif action in {"normal", "n", ""}:
                first = get_number("Enter first number (or ans): ", last_result)
                op = input("Choose operator (+, -, *, /, ^, %): ").strip()
                if op not in OPERATIONS:
                    print("Invalid operator. Use one of: + - * / ^ %")
                    continue
                second = get_number("Enter second number (or ans): ", last_result)
                if op == "/" and second == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = OPERATIONS[op](first, second)
                statement = f"{format_result(first)} {op} {format_result(second)} = {format_result(result)}"
            else:
                print("Unknown mode. Type 'help' to see options.")
                continue

            last_result = float(result)
            timestamp = datetime.now().strftime("%H:%M:%S")
            history.append(f"[{timestamp}] {statement}")
            print(f"Result: {format_result(result)}")

        except ValueError:
            print("Please enter valid numeric values.")
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")
        except ExpressionError as exc:
            print(f"Expression error: {exc}")


if __name__ == "__main__":
    main()
