from jpeg_fuzzer import JPEGFuzzer
import subprocess
import sys

fuzzer = JPEGFuzzer()

fuzzer.take_input('../oskar-smethurst-B1GtwanCbiw-unsplash.jpg')

#mutated = fuzzer.mutation_parameters()
with open("../oskar-smethurst-B1GtwanCbiw-unsplash.jpg", "rb") as f:
    # 1. Load the binary data
    mutated = f.read()


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
