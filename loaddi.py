def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            address, value = line.strip().split(',')
            data.append((address, int(value)))
    return data


def load_instructions(filename):
    instructions = []
    with open(filename, 'r') as file:
        instructions = file.readlines()
    return instructions