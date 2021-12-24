import functools
from typing import Optional

with open("day_24/input.txt") as file:
    INSTRUCTIONS = [line.split() for line in file.readlines()]

MAX_Z = 10 ** 7


@functools.cache
def check_serial(program_counter: int, w: int, x: int, y: int, z: int) -> Optional[str]:
    # Heuristic
    if z > MAX_Z:
        return None

    instruction = INSTRUCTIONS[program_counter]
    regs = {"w": w, "x": x, "y": y, "z": z}

    if instruction[0] == "inp":
        for i in range(9, 0, -1):
            if solution := check_serial(program_counter + 1, i, x, y, z):
                return str(i) + solution
    else:
        op, reg1, reg2 = instruction

        operand1 = regs[reg1]
        try:
            operand2 = int(reg2)
        except ValueError:
            operand2 = regs[reg2]

        match op:
            case "add":
                r = operand1 + operand2
            case "mul":
                r = operand1 * operand2
            case "div":
                r = int(operand1 / operand2)
            case "mod":
                r = operand1 % operand2
            case "eql":
                r = int(operand1 == operand2)
            case _:
                raise ValueError(f"Unknown operation {op!r}")

        regs[reg1] = r

    if program_counter == len(INSTRUCTIONS) - 1:
        return "v" if regs["z"] == 0 else None
    return check_serial(program_counter + 1, **regs)


print(check_serial(0, 0, 0, 0, 0).strip("v"))
