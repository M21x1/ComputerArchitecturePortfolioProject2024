MEMORY_BUS_SIZE = 128

class Memory:
    def __init__(self):
        self.memory_bus = {}
        self.init_memory_bus()
    
    def init_memory_bus(self):
        for b in range(MEMORY_BUS_SIZE):
            self.memory_bus['{0:08b}'.format(b)] = 0
    
    def search_memory_bus(self, address):
        return self.memory_bus.get(address)

    def write_memory_bus(self, address, value):
        if address in self.memory_bus:
            self.memory_bus[address] = value
    
    def load_memory(self, data):
        for address, value in data:
            self.write_memory_bus(address, value)