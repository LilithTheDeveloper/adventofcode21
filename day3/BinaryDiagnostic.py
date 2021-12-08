def load_binary():
    binary = []
    with open('adventofcode21\\day3\\binary.txt') as f:
        lines = f.readlines()
        binary = [line.rstrip() for line in lines]
    return binary

def main():

    gamma_rate = []
    epsilon_rate = []

    length = 12
    size = 0

    binaries = load_binary()
    occurance = []

    for i in range(0, length):
        occurance.append(0)

    for binary in binaries:
        for i in range(0, length):
            if binary[i] == '1':
                occurance[i] += 1
        size += 1
    
    for i in range(0, length):
        if occurance[i] > size/2:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)

    gs = ""
    es = ""

    for bit in gamma_rate:
        gs += str(bit)

    for bit in epsilon_rate:
        es += str(bit)


    print(int(gs, 2))
    print(int(es, 2))
    print(int(gs, 2) * int(es, 2))
            


if __name__ == "__main__":
    main()