import dis
import opcode

def multiply(a,b):
    print(a * b)

multiply(5,5)

# print(multiply.__code__)
# print(multiply.__code__.co_code)

print(dis.dis(multiply))
print(opcode.opmap)