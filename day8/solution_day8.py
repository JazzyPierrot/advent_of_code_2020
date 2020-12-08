
def parse_instruction(instruction):
    """ Parses an instruction to a dictionary """
    splitted_inst = instruction.split(" ")
    inst_dict = {}
    inst_dict[splitted_inst[0]] = int(splitted_inst[1])
    return inst_dict


class program:

    instructions =  []

    _cursor = 0
    _acc = 0
    _program_execution = []


    def __init__(path):
        pass
