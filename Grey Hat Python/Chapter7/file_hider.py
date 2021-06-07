import sys

# Leemos el DLL
fd = open( sys.argv[1], "rb" )
dll_contents = fd.read()
fd.close()
print("[*] Tamaño del: %d" % len( dll_contents ))

# Lo escribimos al ADS
fd = open( "%s:%s" % ( sys.argv[2], sys.argv[1] ), "wb" )
fd.write( dll_contents )
fd.close()