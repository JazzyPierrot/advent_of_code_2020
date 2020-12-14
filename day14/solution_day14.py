import re


neutral_and = int("11111111111111111111111111111111", 2)
neutral_or = 0


class MemoryWriter:

    def __init__(self, instructions=""):
        """
        initialise instructions which should be a string (line)
        generator
        """
        self.instructions = instructions
        self.memory = {}
        self.and_mask = neutral_and
        self.or_mask = neutral_or

    def parse_mask(self, mask_str):
        """
        Parses the mask string and returns an "or_mask" (1s = bits to put to 1)
        and an "and_mask" (0s = bits to put to zero)
        """
        mask = re.findall('[X01]+', mask_str)[0]
        or_mask = int(mask.replace("X", "0"), 2)
        and_mask = int(mask.replace("X", "1"), 2)
        return (or_mask, and_mask)

    def parse_memory_instruction(self, mem_str):
        """
        Parses the memory instruction string and returns (address, value) as
        ints
        """
        address, value = re.findall(r'\d+', mem_str)
        return (int(address), int(value))

    def write_to_memory(self, value, address):
        """ Writes value to address after applying the masks """
        if value < 0 or value >= 2 ** 33:
            raise ValueError
        masked_value = (value & self.and_mask) | self.or_mask
        self.memory[address] = masked_value

    def read_instructions(self):
        """ Reads and apply all instructions """
        for line in self.instructions:
            line = line.strip()
            if line[:3] == "mem":
                address, value = self.parse_memory_instruction(line)
                self.write_to_memory(value, address)
            elif line[:3] == "mas":
                self.or_mask, self.and_mask = self.parse_mask(line)
            else:
                raise ValueError


class MemoryWriterB(MemoryWriter):

    def __init__(self, instructions=""):
        """
        Compared to A, replaces or_mask by floating_or (str) mask
        """
        super().__init__(instructions)
        # neutral floating or
        self.or_mask = "000000000000000000000000000000000000"

    def parse_mask(self, mask_str):
        """
        The or mask is replaced by a floating or, where Xs will take different
        values.
        The and mask puts Xs at 0.
        """
        mask = re.findall('[X01]+', mask_str)[0]
        # and_mask: X => 0 before applying floating, 0, 1 => no change
        and_mask = int(mask.replace("0", "1").replace("X", "0"), 2)
        # floating_or: X => 0 or 1 (floating), 0 => unchanged, 1 => 1
        floating_or_mask = mask
        return (floating_or_mask, and_mask)

    def write_to_memory(self, value, address):
        """
        Writes value at all adresses after applying the masks
        """
        if value < 0 or value >= 2 ** 33:
            raise ValueError
        masked_address = address & self.and_mask
        for a in self.generate_float_addresses(masked_address):
            self.memory[a] = value

    def generate_float_addresses(self, address):
        """
        Generator that iterate over all possible possibilities when replacing
        X with 0 or 1 in floating_or_mask
        """
        yield from self._generate_float_addresses_aux(
            address,
            0,
            # Initialize floating or
            self.or_mask.replace("X", "0")
        )

    def _generate_float_addresses_aux(self, address, min_bit, mask):
        """
        auxiliary function for recursion in generate_float_addresses
        """
        if min_bit == 36:
            yield address | int(mask, 2)
            return
        # No X or X == 0
        yield from self._generate_float_addresses_aux(
            address,
            min_bit + 1,
            mask
        )
        # X == 1
        if self.or_mask[min_bit] == "X":
            temp = list(mask)
            temp[min_bit] = "1"
            mask = "".join(temp)
            yield from self._generate_float_addresses_aux(
                address,
                min_bit + 1,
                mask
            )


if __name__ == "__main__":
    with open("./day14/input.txt") as f:
        mw = MemoryWriter(f)
        mw.read_instructions()
    print("Solution 14A")
    print(sum(mw.memory.values()))

    with open("./day14/input.txt") as f:
        mw = MemoryWriterB(f)
        mw.read_instructions()
    print("Solution 14B")
    print(sum(mw.memory.values()))
