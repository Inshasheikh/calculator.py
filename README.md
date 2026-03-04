# Smart Console Calculator (Python)

A faster and more realistic calculator experience in the terminal.

## Highlights
- **Two input styles**
  - **Normal mode**: enter number + operator + number
  - **Quick mode**: type a full expression like `(12+3)*2/5`
- Supports operators: `+`, `-`, `*`, `/`, `^`, `%`
- `ans` memory to reuse your latest result
- Calculation history (last 10 shown)
- Clean result formatting (e.g., `5` instead of `5.0`)
- Safe expression evaluation using Python AST
- Friendly command menu: `help`, `history`, `clear`, `exit`

## Commands
- `normal` → step-by-step input
- `quick` → expression input
- `history` → show recent calculations
- `clear` → clear history + reset `ans`
- `help` → usage instructions
- `exit` → quit calculator

## Run
```bash
python calculator.py
```

## Example (Quick mode)
```text
Mode [normal/quick/help/history/clear/exit]: quick
Enter expression: (15+5)*2
Result: 40
```
