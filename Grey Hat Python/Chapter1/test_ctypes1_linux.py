# Same as test_ctypes1.py but for Linux
from ctypes import *
libc = CDLL("libc.so.6")
message_string = b"Hello world!\n"
libc.printf("Testing: %s", message_string)