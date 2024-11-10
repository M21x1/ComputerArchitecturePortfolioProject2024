from cache import Cache
from memory import Memory

CPU_COUNTER_INIT_VALUE = 0
NUMBER_OF_REGISTERS = 9

ADD_INSTRUCTION_OPERATOR = "ADD"
ADD_I_INSTRUCTION_OPERATOR = "ADDI"
SUB_INSTRUCTION_OPERATOR = "SUB"
SLT_INSTRUCTION_OPERATOR = "SLT"
BNE_INSTRUCTION_OPERATOR = "BNE"
JUMP_INSTRUCTION_OPERATOR = "J"
JAL_INSTRUCTION_OPERATOR = "JAL"
LW_INSTRUCTION_OPERATOR = "LW"
SW_INSTRUCTION_OPERATOR = "SW"
CACHE_INSTRUCTION_OPERATOR = "CACHE"
HALT_INSTRUCTION_OPERATOR = "HALT"


CACHE_OFF_VALUE = 0
CACHE_ON_VALUE = 1
CACHE_FLUSH_VALUE = 2


def convert_register_to_index(value):
    return int(value[1:]) #

class CPU:
    def __init__(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE
        self.registers = [0]* NUMBER_OF_REGISTERS
        self.cache_flag = False
        self.cache = Cache()
        self.memory_bus = Memory()
        self.running = True
    
    def increment_cpu_counter(self):
        self.cpu_counter += 1
    
    def jump_instruction(self, target):
        self.cpu_counter = int(target)
    
    def add_instruction(self, rd, rs, rt):
        self.registers[convert_register_to_index(rd)] = self.registers[convert_register_to_index(rs)] + self.registers[convert_register_to_index(rt)]
    
    def add_i_instruction(self, rt, rs, immediate):
        self.registers[convert_register_to_index(rt)] = self.registers[convert_register_to_index(rs)] + int(immediate)
    
    def sub_instruction(self, rd, rs, rt):
        self.registers[convert_register_to_index(rd)] = self.registers[convert_register_to_index(rs)] - self.registers[convert_register_to_index(rt)]
    
    def slt_instruction(self, rd, rs, rt):
        self.registers[convert_register_to_index(rd)] = 1 if self.registers[convert_register_to_index(rs)] < self.registers[convert_register_to_index(rt)] else 0 
    
    def bne_instruction(self, rs, rt, offset):
        if self.registers[convert_register_to_index(rs)] != self.registers[convert_register_to_index(rt)]:
            self.cpu_counter += int(offset) * 4
    
    def jal_instruction(self, target):
        self.registers[7] = self.cpu_counter + 4
        self.cpu_counter = int(target) * 4
    
    def lw_instruction(self, rt, offset, rs):
        address = self.registers[convert_register_to_index(rs)] + int(offset)
        value = self.memory_bus.search_memory_bus('{0:08b}'.format(address))
        self.registers[convert_register_to_index(rt)] = value

    def sw_instruction(self, rt, offset, rs):
        address = self.registers[convert_register_to_index(rs)] + int(offset)
        self.memory_bus.write_memory_bus('{0:08b}'.format(address), self.registers[convert_register_to_index(rt)])
    
    def cache_instruction(self, code):
        if int(code) == CACHE_OFF_VALUE:
            self.cache_flag = False
        elif int(code) == CACHE_ON_VALUE:
            self.cache_flag = True
        elif int(code) == CACHE_FLUSH_VALUE:
            self.cache.flush_cache()
    
    def halt_instruction(self):
        self.running = False
        
    def parse_instruction(self, instruction):
        parts = instruction.split()
        op = parts[0]
        operands = parts[1:] if len(parts) > 1 else []
        
        print(f"Executing instruction: {instruction}")
        
        if op == ADD_INSTRUCTION_OPERATOR:
            self.add_instruction(*operands)
        elif op == ADD_I_INSTRUCTION_OPERATOR:
            self.add_i_instruction(*operands)
        elif op == SUB_INSTRUCTION_OPERATOR:
            self.sub_instruction(*operands)
        elif op == SLT_INSTRUCTION_OPERATOR:
            self.slt_instruction(*operands)
        elif op == BNE_INSTRUCTION_OPERATOR:
            self.bne_instruction(*operands)
        elif op == JUMP_INSTRUCTION_OPERATOR:
            self.jump_instruction(*operands)
        elif op == JAL_INSTRUCTION_OPERATOR:
            self.jal_instruction(*operands)
        elif op == LW_INSTRUCTION_OPERATOR:
            self.lw_instruction(*operands)
        elif op == SW_INSTRUCTION_OPERATOR:
            self.sw_instruction(*operands)
        elif op == CACHE_INSTRUCTION_OPERATOR:
            self.cache_instruction(*operands)
        elif op == HALT_INSTRUCTION_OPERATOR:
            self.halt_instruction()
        self.increment_cpu_counter()
    
    def load_instructions(self, instructions):
        for instruction in instructions:
            if not self.running:
                break
            self.parse_instruction(instruction.strip())    
    
    def load_memory(self, data):
        self.memory_bus.load_memory(data)