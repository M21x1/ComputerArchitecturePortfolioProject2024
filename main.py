from cpu import CPU
from loaddi import load_data,load_instructions

def main():
    cpu = CPU()
    
    # loading initial memory values
    memory_data = load_data('data_input.txt')
    cpu.load_memory(memory_data)
    
    #loading and executing instructions
    instructions = load_instructions('instruction_input.txt')
    cpu.load_instructions(instructions)
    
    # Output final CPU state
    print("Final CPU state:")
    print(f"Registers: {cpu.registers}")
    print(f"Program Counter: {cpu.cpu_counter}")
    print("Memory Bus:")
    for address, value in cpu.memory_bus.memory_bus.items():
        print(f"Address: {address}, Value: {value}")


#if __name__ == "__main__":
#    main()

main()