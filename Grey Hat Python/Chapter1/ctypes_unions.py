from ctypes import *

# Defining a C Union

# In C
# union {
#   long barley_long;
#   int barley_int;
#   char barley_char[8];
# } barley_amount;

# In Python
class barley_amount(Union):
    _fields_ = [
        ("barley_long", c_long), 
        ("barley_int", c_int),
        ("barley_char", c_char*8), 
    ]
