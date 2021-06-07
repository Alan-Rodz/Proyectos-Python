from ctypes import *

# Defining a C Structure

# C
# struct beer_recipe
# {
#   int amt_barley;
#   int amt_water;
# }

# Python (through c types)
class beer_recipe(Structure):
    _fields_ = [
        ("amt_barley", c_int),
        ("amt_water", c_int)
    ]