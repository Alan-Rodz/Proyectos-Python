import sys
from ctypes import *

PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF )
VIRTUAL_MEM = ( 0x1000 | 0x2000 )

kernel32 = windll.kernel32
pid = sys.argv[1]
dll_path = sys.argv[2]
dll_len = len(dll_path)

# Obtenemos un handle al proceso donde nos estamos inyectando
h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(pid) )

if( not h_process):
    print ("[*] No se pudo obtener un handle al PID: %s" % pid)
    sys.exit(0)

# Alocamos espacio para el DLL path 
arg_address = kernel32.VirtualAllocEx(h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

# Escribimos el DLL path en el espacio alocado
written = c_int(0)
kernel32.WriteProcessMemory(h_process, arg_address, dll_path, dll_len, byref(written))

# Obtenemos la direccion de LoadLibraryA
h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
h_loadlib = kernel32.GetProcAddress(h_kernel32,"LoadLibraryA")

# Tratamos de crear el threaed remoto con el punto de entrada establecido en 
# LoadLibraryA y un puntero al DLL path comom su unico parametro
thread_id = c_ulong(0)
if not kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib,arg_address, 0, byref(thread_id)):
    print ("[*] No se pudo inyectar el DLL. Saliendo...")
    sys.exit(0)