import capstone
import any_capstone


dis = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32)

def PROCESSOR_ENTRY():
    return any_capstone.Processor("x86_32", dis)
