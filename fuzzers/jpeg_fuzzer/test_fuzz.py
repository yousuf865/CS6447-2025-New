from jpeg_fuzzer import JPEGFuzzer
import subprocess
import sys
from pwn import *

p = process('binaries/jpg1')

#fuzzer = JPEGFuzzer()

#fuzzer.take_input('../oskar-smethurst-B1GtwanCbiw-unsplash.jpg')

#mutated = fuzzer.mutation_parameters()
with open("../oskar-smethurst-B1GtwanCbiw-unsplash.jpg", "rb") as f:
    # 1. Load the binary data
    mutated = f.read()

p.send(mutated)
p.interactive()
'''
try:
    sys.stdout.buffer.write(mutated)
    sys.stdout.buffer.flush()

except BrokenPipeError:
    # Handle the error and exit gracefully
    try:
        sys.stdout.close()
    except:
        pass
    sys.exit(0)
'''
