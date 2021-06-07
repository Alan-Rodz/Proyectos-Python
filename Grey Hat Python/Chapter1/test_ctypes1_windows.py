from ctypes import * 

# (Windows/DOS only) 
# The msvcrt module gives you access to a number of functions in the Microsoft Visual C/C++ Runtime Library (MSVCRT).
# The cdll() method is used for loading libraries that export functions using the standard cdecl calling convention
# The cdecl (which stands for C declaration) is a calling convention that originates from Microsoft's compiler for the C programming language 
# It is used by many C compilers for the x86 architecture.
# https://www.youtube.com/watch?v=frqPX7EHscM&ab_channel=VikramSalunke explains cdecl
msvcrt = CDLL('msvcrt')
message_string = b"Hello World!\n"
msvcrt.printf(b"Testing: %s\n", message_string)