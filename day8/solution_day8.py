import copy


def parse_instruction(instruction):
    """ Parses an instruction to a dictionary """
    splitted_inst = instruction.split(" ")
    return (splitted_inst[0], int(splitted_inst[1]))


class Program:

    def __init__(self, instructions):
        self._instructions = []  # List of instructions
        self._cursor = 0  # Position of the next instruction to be executed
        self._acc = 0  # Value of accumulative variable
        # History of positions of the already executed instructions
        self._program_execution = []
        self._instructions = instructions

    @classmethod
    def from_string(cls, instructions):
        """ Reads program from string """
        return cls([parse_instruction(inst)
                    for inst in instructions.splitlines()])

    @classmethod
    def from_file(cls, path):
        """ Reads program from file"""
        with open(path) as f:
            return cls([parse_instruction(line.strip())
                        for line in f])

    def reset(self):
        """ Resets the program at its start without changing the
        instructions """
        self._acc = 0
        self._cursor = 0
        self._program_execution = []

    def exe_instruction(self):
        """ Executes the next instruction (the one at the cursor position),
        and update the _cursor, _acc and _program_execution attributes
        accordingly
        """
        if self._cursor < 0 or self._cursor >= len(self._instructions):
            raise ValueError("Trying to execute an invalid line")
        self._program_execution.append(self._cursor)
        current_inst = self._instructions[self._cursor]
        if current_inst[0] == "jmp":
            self._jump(current_inst[1])
        elif current_inst[0] == "acc":
            self._accumulate(current_inst[1])
        elif current_inst[0] == "nop":
            self._nop()
        else:
            raise ValueError(f"Instruction {current_inst[0]} not known")

    def execute(self):
        """ Executes the program until the end. If it returns on a line
        already visited, the program raises a RecursionError."""
        while True:
            if self._cursor in self._program_execution:
                raise RecursionError("Program entered an infinite loop")
            if self._cursor == len(self._instructions):
                break
            self.exe_instruction()
        print("Program executed with success")

    # Instructions

    def _jump(self, value):
        """ `jmp` instruction """
        self._cursor += value

    def _accumulate(self, value):
        """ `acc` instruction """
        self._cursor += 1
        self._acc += value

    def _nop(self):
        """ `nop` instruction """
        self._cursor += 1


def switch_instruction(prg, instruction_pos):
    changed_prg = copy.deepcopy(prg)
    instruction = prg._instructions[instruction_pos]
    if instruction[0] == "jmp":
        changed_prg._instructions[instruction_pos] = ("nop", instruction[1])
    elif instruction[0] == "nop":
        changed_prg._instructions[instruction_pos] = ("jmp", instruction[1])
    else:
        raise ValueError
    return changed_prg


if __name__ == "__main__":
    prg = Program.from_file("./day8/input.txt")
    try:
        prg.execute()
    except RecursionError:
        print("Solution 8A:")
        print("------------")
        print("Program entered an infinite loop")
        print(f"Accumulator value: {prg._acc}")

    print()
    prg.reset()
    pos_possibly_corrupt = (inst_pos
                            for inst_pos, inst in enumerate(prg._instructions)
                            if inst[0] == "nop" or inst[0] == "jmp")
    for inst_position in pos_possibly_corrupt:
        try:
            new_prog = switch_instruction(prg, inst_position)
            new_prog.execute()
            print("Solution 8B")  # If no error: success.
            print("-----------")
            print(
                f"Switching instructions at position {inst_position} makes the"
                f" program work until the end"
            )
            print(f"Accumulator value: {new_prog._acc}")
            break
        except RecursionError:
            next  # Try another instruction switch
