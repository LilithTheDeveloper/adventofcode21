

#Read commands from file
def load_commands():
    commands = []
    with open('adventofcode21\day2\commands.txt') as f:
        lines = f.readlines()
        commands = [line.rstrip() for line in lines]
    return commands

class submarine:
    depth = 0
    progression = 0
    aim = 0

    def __init__(self) -> None:
        pass

    def forward(self, amount:int):
        self.progression += amount
        self.depth += self.aim*amount

    def up(self, amount:int):
        self.aim -= amount

    def down(self, amount:int):
        self.aim += amount

    def print_pos(self):
        print("Depth: {}".format(self.depth))
        print("Progression: {}".format(self.depth))
        print("Result: {}".format(self.depth*self.progression))

def main():
    sub = submarine()
    commands = load_commands()

    for args in commands:
        args = args.split(' ')

        cmd = args[0]
        amount = int(args[1])
        
        
        match cmd:
            case "forward":
                sub.forward(amount)
            case "up":
                sub.up(amount)
            case "down":
                sub.down(amount)
            case _:
                pass

    sub.print_pos()

if __name__ == "__main__":
    main()