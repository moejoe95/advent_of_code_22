import math

monkeys = {}


class Monkey():
    def __init__(self, items, operation, test_val, next_true, next_false) -> None:
        self.items = [i for i in reversed(items)]
        self.operation = operation
        self.test_val = test_val
        self.next_true = next_true
        self.next_false = next_false
        self.item_count = 0

    def do_monkey_things(self):
        while len(self.items) > 0:
            item = self.items.pop()
            item = eval(self.operation, {}, {'old': item})
            item = item // 3
            self.throw(item)
            self.item_count += 1

    def throw(self, item):
        if item % self.test_val == 0:
            monkeys[self.next_true].items.append(item)
        else:
            monkeys.get(self.next_false).items.append(item)


with open('input11.txt', 'r') as f:
    lines = [l for l in reversed(f.readlines())]
    while len(lines) > 0:
        line = lines.pop()
        if line.startswith('Monkey'):
            id = line.split(' ')[1][0]
            items = [int(i)
                     for i in lines.pop().strip().split(':')[1].split(',')]
            op = lines.pop().strip().split('=')[1].strip()
            test = int(lines.pop().strip().split(' ')[-1])
            next_true = lines.pop().strip().split(' ')[-1]
            next_false = lines.pop().strip().split(' ')[-1]
            monkeys[id] = Monkey(items, op, test, next_true, next_false)
        if len(line.strip()) == 0:
            continue


for i in range(0, 20):
    for id in monkeys.keys():
        monkeys.get(id).do_monkey_things()
    if i % 1000 == 0:
        print('done with round:', i)

monkey_list = [monkeys[id] for id in monkeys.keys()]
monkey_list.sort(key=lambda x: x.item_count, reverse=True)
monkey_business = math.prod(m.item_count for m in monkey_list[0:2])
print(monkey_business)
