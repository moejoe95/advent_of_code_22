
class Executor():
    def __init__(self) -> None:
        self.cycle_times = {'addx': 2, 'noop': 1}
        self.inst_count = 0
        self.register = 1

    def execute(self, instruction) -> None:
        if self.is_ready():
            self.inst_count = self.cycle_times.get(instruction[0])
        self.inst_count -= 1
        if instruction[0] == 'addx' and self.is_ready():
            self.register += int(instruction[1])

    def is_ready(self) -> bool:
        return self.inst_count == 0


class Display():
    def __init__(self) -> None:
        self.current_row = ['.'] * 40
        self.current_pos = 0

    def render(self, register):
        if self.current_pos in range(register-1, register+2):
            self.current_row[self.current_pos] = '#'
        self.current_pos += 1
        if self.current_pos >= 40:
            print(''.join(self.current_row))
            self.current_pos = 0
            self.current_row = ['.'] * 40


class Emulator():
    def __init__(self, executor, cycles_to_calc, display) -> None:
        self.executor = executor
        self.cycle = 0
        self.sum_signal_strengh = 0
        self.cycles_to_calc = cycles_to_calc
        self.display = display

    def emulate(self, instructions):
        instructions = [i for i in reversed(instructions)]
        while len(instructions) > 0 or not self.executor.is_ready():
            self.cycle += 1
            if self.cycle in self.cycles_to_calc:
                self.sum_signal_strengh = self.sum_signal_strengh + \
                    self.cycle * self.executor.register
            if self.executor.is_ready():
                instruction = instructions.pop()
            self.display.render(self.executor.register)
            self.executor.execute(instruction)


instructions = []
with open('input10.txt', 'r') as f:
    for line in f.readlines():
        instructions.append(line.strip().split(' '))

emulator = Emulator(Executor(), [20, 60, 100, 140, 180, 220], Display())
emulator.emulate(instructions)
print('summed signal strenght: ', emulator.sum_signal_strengh)
