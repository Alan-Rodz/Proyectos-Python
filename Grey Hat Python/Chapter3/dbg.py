from ctypes import *
import sys
import time
from ctypes import *

# Mapeando los tipos Microsoft a los tipos de ctypes
BYTE      = c_ubyte
WORD      = c_ushort
DWORD     = c_ulong
LPBYTE    = POINTER(c_ubyte)
LPTSTR    = POINTER(c_char) 
HANDLE    = c_void_p
PVOID     = c_void_p
LPVOID    = c_void_p
UINT_PTR  = c_ulong
SIZE_T    = c_ulong

# Constantes
DEBUG_PROCESS         = 0x00000001
CREATE_NEW_CONSOLE    = 0x00000010
PROCESS_ALL_ACCESS    = 0x001F0FFF
INFINITE              = 0xFFFFFFFF
DBG_CONTINUE          = 0x00010002
DBG_EXCEPTION_NOT_HANDLED = 0x00000000

# Constantes de evento de debugeo
EXCEPTION_DEBUG_EVENT      =    0x1
CREATE_THREAD_DEBUG_EVENT  =    0x2
CREATE_PROCESS_DEBUG_EVENT =    0x3
EXIT_THREAD_DEBUG_EVENT    =    0x4
EXIT_PROCESS_DEBUG_EVENT   =    0x5
LOAD_DLL_DEBUG_EVENT       =    0x6
UNLOAD_DLL_DEBUG_EVENT     =    0x7
OUTPUT_DEBUG_STRING_EVENT  =    0x8
RIP_EVENT                  =    0x9

# Codigos de excepcion de debugeo
EXCEPTION_ACCESS_VIOLATION     = 0xC0000005
EXCEPTION_BREAKPOINT           = 0x80000003
EXCEPTION_GUARD_PAGE           = 0x80000001
EXCEPTION_SINGLE_STEP          = 0x80000004

# Constantes thread para CreateToolhelp32Snapshot()
TH32CS_SNAPHEAPLIST = 0x00000001
TH32CS_SNAPPROCESS  = 0x00000002
TH32CS_SNAPTHREAD   = 0x00000004
TH32CS_SNAPMODULE   = 0x00000008
TH32CS_INHERIT      = 0x80000000
TH32CS_SNAPALL      = (TH32CS_SNAPHEAPLIST | TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD | TH32CS_SNAPMODULE)
THREAD_ALL_ACCESS   = 0x001F03FF

# Context flags for GetThreadContext()
CONTEXT_FULL                   = 0x00010007
CONTEXT_DEBUG_REGISTERS        = 0x00010010

# Permisos de Memoria
PAGE_EXECUTE_READWRITE         = 0x00000040

# Condiciones para breakpoints de Hardware
HW_ACCESS                      = 0x00000003
HW_EXECUTE                     = 0x00000000
HW_WRITE                       = 0x00000001

# Permisos de pagina de Memoria usados por VirtualProtect()
PAGE_NOACCESS                  = 0x00000001
PAGE_READONLY                  = 0x00000002
PAGE_READWRITE                 = 0x00000004
PAGE_WRITECOPY                 = 0x00000008
PAGE_EXECUTE                   = 0x00000010
PAGE_EXECUTE_READ              = 0x00000020
PAGE_EXECUTE_READWRITE         = 0x00000040
PAGE_EXECUTE_WRITECOPY         = 0x00000080
PAGE_GUARD                     = 0x00000100
PAGE_NOCACHE                   = 0x00000200
PAGE_WRITECOMBINE              = 0x00000400

# Structs para la funcion CreateProcessA()
# STARTUPINFO describe como spawnear el proceso
class STARTUPINFO(Structure):
    _fields_ = [
        ("cb",            DWORD),        
        ("lpReserved",    LPTSTR), 
        ("lpDesktop",     LPTSTR),  
        ("lpTitle",       LPTSTR),
        ("dwX",           DWORD),
        ("dwY",           DWORD),
        ("dwXSize",       DWORD),
        ("dwYSize",       DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",       DWORD),
        ("wShowWindow",   WORD),
        ("cbReserved2",   WORD),
        ("lpReserved2",   LPBYTE),
        ("hStdInput",     HANDLE),
        ("hStdOutput",    HANDLE),
        ("hStdError",     HANDLE),
        ]

# PROCESS_INFORMATION recibe su informacion despues de que el proceso en cuestion ha sido iniciado exitosamente
class PROCESS_INFORMATION(Structure):
    _fields_ = [
        ("hProcess",    HANDLE),
        ("hThread",     HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId",  DWORD),
        ]

# Cuando el dwDebugEventCode es evaluado
class EXCEPTION_RECORD(Structure):
    pass

EXCEPTION_RECORD._fields_ = [
        ("ExceptionCode",        DWORD),
        ("ExceptionFlags",       DWORD),
        ("ExceptionRecord",      POINTER(EXCEPTION_RECORD)),
        ("ExceptionAddress",     PVOID),
        ("NumberParameters",     DWORD),
        ("ExceptionInformation", UINT_PTR * 15),
        ]

class _EXCEPTION_RECORD(Structure):
    _fields_ = [
        ("ExceptionCode",        DWORD),
        ("ExceptionFlags",       DWORD),
        ("ExceptionRecord",      POINTER(EXCEPTION_RECORD)),
        ("ExceptionAddress",     PVOID),
        ("NumberParameters",     DWORD),
        ("ExceptionInformation", UINT_PTR * 15),
        ]

# Excepciones
class EXCEPTION_DEBUG_INFO(Structure):
    _fields_ = [
        ("ExceptionRecord",    EXCEPTION_RECORD),
        ("dwFirstChance",      DWORD),
        ]

# Llena esta union de manera apropiada
class DEBUG_EVENT_UNION(Union):
    _fields_ = [
        ("Exception",         EXCEPTION_DEBUG_INFO),
#        ("CreateThread",      CREATE_THREAD_DEBUG_INFO),
#        ("CreateProcessInfo", CREATE_PROCESS_DEBUG_INFO),
#        ("ExitThread",        EXIT_THREAD_DEBUG_INFO),
#        ("ExitProcess",       EXIT_PROCESS_DEBUG_INFO),
#        ("LoadDll",           LOAD_DLL_DEBUG_INFO),
#        ("UnloadDll",         UNLOAD_DLL_DEBUG_INFO),
#        ("DebugString",       OUTPUT_DEBUG_STRING_INFO),
#        ("RipInfo",           RIP_INFO),
        ]   

# Describe un evento de debuggeo que el debuggeador ha atrapado
class DEBUG_EVENT(Structure):
    _fields_ = [
        ("dwDebugEventCode", DWORD),
        ("dwProcessId",      DWORD),
        ("dwThreadId",       DWORD),
        ("u",                DEBUG_EVENT_UNION),
        ]

# Usado por el struct CONTEXT
class FLOATING_SAVE_AREA(Structure):
   _fields_ = [
   
        ("ControlWord", DWORD),
        ("StatusWord", DWORD),
        ("TagWord", DWORD),
        ("ErrorOffset", DWORD),
        ("ErrorSelector", DWORD),
        ("DataOffset", DWORD),
        ("DataSelector", DWORD),
        ("RegisterArea", BYTE * 80),
        ("Cr0NpxState", DWORD),
]

# El struct CONTEXT, que contiene todos los valores de los registros despues de una llamada a GetThreadContext()
class CONTEXT(Structure):
    _fields_ = [
    
        ("ContextFlags", DWORD),
        ("Dr0", DWORD),
        ("Dr1", DWORD),
        ("Dr2", DWORD),
        ("Dr3", DWORD),
        ("Dr6", DWORD),
        ("Dr7", DWORD),
        ("FloatSave", FLOATING_SAVE_AREA),
        ("SegGs", DWORD),
        ("SegFs", DWORD),
        ("SegEs", DWORD),
        ("SegDs", DWORD),
        ("Edi", DWORD),
        ("Esi", DWORD),
        ("Ebx", DWORD),
        ("Edx", DWORD),
        ("Ecx", DWORD),
        ("Eax", DWORD),
        ("Ebp", DWORD),
        ("Eip", DWORD),
        ("SegCs", DWORD),
        ("EFlags", DWORD),
        ("Esp", DWORD),
        ("SegSs", DWORD),
        ("ExtendedRegisters", BYTE * 512),
]

# THREADENTRY32 contiene informacion sobre un thread
# Usamos esto para enumerar todos los threads del sistema 
class THREADENTRY32(Structure):
    _fields_ = [
        ("dwSize",             DWORD),
        ("cntUsage",           DWORD),
        ("th32ThreadID",       DWORD),
        ("th32OwnerProcessID", DWORD),
        ("tpBasePri",          DWORD),
        ("tpDeltaPri",         DWORD),
        ("dwFlags",            DWORD),
    ]

# Struct de soporte para la union SYSTEM_INFO_UNION
class PROC_STRUCT(Structure):
    _fields_ = [
        ("wProcessorArchitecture",    WORD),
        ("wReserved",                 WORD),
]

# Union de soporte para el struct SYSTEM_INFO
class SYSTEM_INFO_UNION(Union):
    _fields_ = [
        ("dwOemId",    DWORD),
        ("sProcStruc", PROC_STRUCT),
]

# El struct SYSTEM_INFO se llena cuando se realiza una llamada a kernel32.GetSystemInfo()
# Usamos dwPageSize para hacer calculos cuando usamos breakpoints de memoria
class SYSTEM_INFO(Structure):
    _fields_ = [
        ("uSysInfo", SYSTEM_INFO_UNION),
        ("dwPageSize", DWORD),
        ("lpMinimumApplicationAddress", LPVOID),
        ("lpMaximumApplicationAddress", LPVOID),
        ("dwActiveProcessorMask", DWORD),
        ("dwNumberOfProcessors", DWORD),
        ("dwProcessorType", DWORD),
        ("dwAllocationGranularity", DWORD),
        ("wProcessorLevel", WORD),
        ("wProcessorRevision", WORD),
]

# MEMORY_BASIC_INFORMATION contiene informacion sobre una region particular de memoria
# Una llamdada a kernel32.VirtualQuery() llena este estruct
class MEMORY_BASIC_INFORMATION(Structure):
    _fields_ = [
        ("BaseAddress", PVOID),
        ("AllocationBase", PVOID),
        ("AllocationProtect", DWORD),
        ("RegionSize", SIZE_T),
        ("State", DWORD),
        ("Protect", DWORD),
        ("Type", DWORD),
]

# Kernel
kernel32 = windll.kernel32

class debugger():

    def __init__(self):
        self.h_process       =     None
        self.pid             =     None
        self.debugger_active =     False
        self.h_thread        =     None
        self.context         =     None
        self.breakpoints     =     {}
        self.first_breakpoint=     True
        self.hardware_breakpoints = {}
        
        # Determinamos y guardamos el tamaño de pagina default del sistema 
        system_info = SYSTEM_INFO()
        kernel32.GetSystemInfo(byref(system_info))
        self.page_size = system_info.dwPageSize
        
        # TODO: test
        self.guarded_pages      = []
        self.memory_breakpoints = {}
        
    def cargar(self,path_to_exe):
        
        # dwCreation determina como crear el proceso
        creation_flags = DEBUG_PROCESS
    
        # instanciamos los structs
        startupinfo         = STARTUPINFO()
        process_information = PROCESS_INFORMATION()
        
        # Las siguientes dos opciones le permiten al proceso iniciado ser mostrado en una ventana separada
        # Tambien ilustra como las diferentes configuraciones en el struct STARTUPINFO pueden afectar el programa debuggeado
        startupinfo.dwFlags     = 0x1
        startupinfo.wShowWindow = 0x0
        
        # Inicializamos la variable cb en el struct STARTUPINFO, que es el tamaño del struct en si mismo
        startupinfo.cb = sizeof(startupinfo)
        
        if kernel32.CreateProcessA(path_to_exe,None,None,None,None,creation_flags,None,None,byref(startupinfo),byref(process_information)):
            print("[*] Hemos iniciado el proceso de manera exitosa!")
            print("[*] El ID del proceso es: %d" % process_information.dwProcessId)
            self.pid = process_information.dwProcessId
            self.h_process = self.abrir_proceso(self,process_information.dwProcessId)
            self.debugger_active = True
        else:    
            print ("[*] Error con código %d." % kernel32.GetLastError())

    def abrir_proceso(self,pid):
        # PROCESS_ALL_ACCESS = 0x0x001F0FFF
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid) 
        return h_process
            
    def adjuntar(self,pid):
        self.h_process = self.abrir_proceso(pid)
        
        # Intentamos adjuntarnos al proceso, si esto falla regresamos de la llamada
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid             = int(pid)
        else:
            print ("[*] El debugger no pudo adjuntarse al proceso.")
        
    def ejecutar(self):
        # Esperamos eventos de debuggeo en el proceso que esta siendo debuggeado
        while self.debugger_active == True:
            self.obtener_evento_de_debuggeo() 
            
    def obtener_evento_de_debuggeo(self):
        evento_de_debuggeo    = DEBUG_EVENT()
        estatus_de_continuacion = DBG_CONTINUE
                                  
        if kernel32.WaitForDebugEvent(byref(evento_de_debuggeo),100):
        
            # Obtenemos informacion con respecto a la excepcion
            self.h_thread          = self.abrir_thread(evento_de_debuggeo.dwThreadId)
            self.context           = self.obtener_contexto_del_thread(h_thread=self.h_thread)
            self.debug_event       = evento_de_debuggeo
            print("Codigo de Evento: %d ID del Thread: %d" % (evento_de_debuggeo.dwDebugEventCode,evento_de_debuggeo.dwThreadId))
        
            if evento_de_debuggeo.dwDebugEventCode == EXCEPTION_DEBUG_EVENT:
                self.exception = evento_de_debuggeo.u.Exception.ExceptionRecord.ExceptionCode
                self.exception_address = evento_de_debuggeo.u.Exception.ExceptionRecord.ExceptionAddress
        
                # llamamos al handler interno para el evento de excepcion que ocurrio    
                if self.exception == EXCEPTION_ACCESS_VIOLATION:
                    print ("Violacion de Acceso Detectada.")
                elif self.exception == EXCEPTION_BREAKPOINT:
                    estatus_de_continuacion = self.breakpoint_exception_handler()
                elif self.exception == EXCEPTION_GUARD_PAGE:
                    print ("Acceso a Pagina de Guardia Detectado.")
                elif self.exception == EXCEPTION_SINGLE_STEP:
                    self.exception_handler_paso_singular()
                
            kernel32.ContinueDebugEvent(evento_de_debuggeo.dwProcessId, evento_de_debuggeo.dwThreadId, estatus_de_continuacion)
                       
    def despegar(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print ("[*] Se ha terminado de debuggear. Saliendo...")
            return True
        else:
            print ("Hubo un error tratando de despegar el debugger del proceso debuggeado.")
            return False
            
    def abrir_thread (self, thread_id):
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, thread_id)
        if h_thread is not None:
            return h_thread
        else:
            print ("[*] No se pudo obtener un thread handle valido....")
            return False
        
    def enumerar_threads(self):
        thread_entry     = THREADENTRY32()
        lista_threads      = []
        snapshot         = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)
        
        if snapshot is not None:
            
            # Tenemos que establecer el tamaño del struct o la llamada fallara
            thread_entry.dwSize = sizeof(thread_entry)
            success = kernel32.Thread32First(snapshot, byref(thread_entry))

            while success:
                if thread_entry.th32OwnerProcessID == self.pid:
                    lista_threads.append(thread_entry.th32ThreadID)

                success = kernel32.Thread32Next(snapshot, byref(thread_entry))
            
            # Cierra los handles para que no se filtren
            kernel32.CloseHandle(snapshot)
            return lista_threads
        else:
            return False
        
    def obtener_contexto_del_thread (self, thread_id=None,h_thread=None):
        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        
        # Obtenemos un handle al thread
        if h_thread is None:
            self.h_thread = self.abrir_thread(thread_id)
                        
        if kernel32.GetThreadContext(self.h_thread, byref(context)):
            
            return context 
        else:
            return False
    
    def leer_memoria_del_proceso(self,address,length):
        informacion         = ""
        buffer_lectura     = create_string_buffer(length)
        cuenta        = c_ulong(0)
        kernel32.ReadProcessMemory(self.h_process, address, buffer_lectura, 5, byref(cuenta))
        informacion    = buffer_lectura.raw
        return informacion
        
    def escribir_a_memoria_del_proceso(self,address,data):
        cuenta  = c_ulong(0)
        longitud = len(data)
        c_informacion = c_char_p(data[cuenta.value:])
        if not kernel32.WriteProcessMemory(self.h_process, address, c_informacion, longitud, byref(cuenta)):
            return False
        else:
            return True
            
    def set_breakpoint(self,direccion):
        print ("[*] Establenciendo breakpoint en : 0x%08x" % direccion)
        if not self.breakpoints.has_key(direccion):

            # Guardamos el byte original
            old_protect = c_ulong(0)
            kernel32.VirtualProtectEx(self.h_process, direccion, 1, PAGE_EXECUTE_READWRITE, byref(old_protect))
            byte_original = self.leer_memoria_del_proceso(direccion, 1)
            
            if byte_original != False:
                
                # Escribimos el opcode INT3
                if self.escribir_a_memoria_del_proceso(direccion, "\xCC"):
                    
                    # register the breakpoint in our internal list
                    # Registramos el breakpoint en nuestra lista interna
                    self.breakpoints[direccion] = byte_original
                    return True
            else:
                return False

    def breakpoint_exception_handler(self):
        print("[*] Direccion de la Excepcion: 0x%08x" % self.exception_address)
        # Checamos si el breakpoint es alguno de los que pusimos nosotros
        if not self.breakpoints.__contains__(self.exception_address):
           
                # Si es el primer breakpoint puesto por Windows simplemente continuamos
                if self.first_breakpoint == True:
                   self.first_breakpoint = False
                   print("[*] Se alcanzo el primer breakpoint.")
                   return DBG_CONTINUE
               
        else:
            print("[*] Se alcanzo un breakpoint establecido por el usuario.")
            # Aqui es donde manejamos los breakpoints que nosotros establecimos
            # Primero ponemos el byte original de regreso
            self.escribir_a_memoria_del_proceso(self.exception_address, self.breakpoints[self.exception_address])

            # Obtenemos un registro de contexto nuevo, reseteamos EIP al byte original y luego
            # ponemos el contexto del thread con el nuevo valor del EIP
            self.context = self.obtener_contexto_del_thread(h_thread=self.h_thread)
            self.context.Eip -= 1
            kernel32.SetThreadContext(self.h_thread,byref(self.context))
            estatus_continuacion = DBG_CONTINUE
            
        return estatus_continuacion
            
    def resolucion_de_funciones(self,dll,function):
        handle  = kernel32.GetModuleHandleA(dll)
        direccion = kernel32.GetProcAddress(handle, function)
        kernel32.CloseHandle(handle)
        return direccion
        
    def breakpoint_set_hardware(self, address, length, condition):
        
        # Checamos que el valor de la longitud sea valido
        if length not in (1, 2, 4):
            return False
        else:
            length -= 1
            
        # Checamos que la condicion sea valida
        if condition not in (HW_ACCESS, HW_EXECUTE, HW_WRITE):
            return False
        
        # Checamos los lugares disponibles
        if not self.hardware_breakpoints.__contains__(0):
            available = 0
        elif not self.hardware_breakpoints.__contains__(1):
            available = 1
        elif not self.hardware_breakpoints.__contains__(2):
            available = 2
        elif not self.hardware_breakpoints.__contains__(3):
            available = 3
        else:
            return False

        # Queremos modificar el registro de debuggeo en cada thread
        for thread_id in self.enumerar_threads():
            context = self.obtener_contexto_del_thread(thread_id=thread_id)

            # Activamos la bandera apropiada en el registro DR7 para poner el breakpoint
            context.Dr7 |= 1 << (available * 2)

            # Guardamos la direccion del breakpoint en el registro libre que encontramos 
            if   available == 0: context.Dr0 = address
            elif available == 1: context.Dr1 = address
            elif available == 2: context.Dr2 = address
            elif available == 3: context.Dr3 = address

            # Establecemos la condicion del breakpoint
            context.Dr7 |= condition << ((available * 4) + 16)

            # Establecemos la longitud
            context.Dr7 |= length << ((available * 4) + 18)

            # Hacemos que el contexto de este thread sea el mismo que el de los registros de debuggeo
            h_thread = self.abrir_thread(thread_id)
            kernel32.SetThreadContext(h_thread,byref(context))

        # Actualizamos el arreglo de breakpoints de hardware internos en el indice del lugar (slot)
        self.hardware_breakpoints[available] = (address,length,condition)

        return True
    
    def exception_handler_paso_singular(self):
        print ("[*] Exception address: 0x%08x" % self.exception_address)

        # Determinamos si este evento de paso singular ocurrio en reaccion a un breakpoint de hardware y obtenemos el hit breakpoint
        # De acuerdo a la documenacion de Intel deberiamos ser capaces de checar la bandera BS en DR6
        # Pero parece que Windows no esta propagando esta bandera apropiadamente 
        if self.context.Dr6 & 0x1 and self.hardware_breakpoints.__contains__(0):
            slot = 0
        elif self.context.Dr6 & 0x2 and self.hardware_breakpoints.__contains__(1):
            slot = 0
        elif self.context.Dr6 & 0x4 and self.hardware_breakpoints.__contains__(2):
            slot = 0
        elif self.context.Dr6 & 0x8 and self.hardware_breakpoints.__contains__(3):
            slot = 0
        else:
            # No se trata de un INT1 generado por un breakpoint de hardware
            estatus_continuacion = DBG_EXCEPTION_NOT_HANDLED

        # Removemos el breakpoint de la lista de breakpoints
        if self.breakpoint_borrar_hardware(slot):
            estatus_continuacion = DBG_CONTINUE

        print ("[*] Breakpoint de Hardware removido.")
        return estatus_continuacion

    def breakpoint_borrar_hardware(self,slot):
        
        # Desactivamos el breakpoint para todos los threads activos
        for thread_id in self.enumerar_threads():
            contexto = self.obtener_contexto_del_thread(thread_id=thread_id)
            
            # Reiniciamos las banderas para remover el breakpoint            
            contexto.Dr7 &= ~(1 << (slot * 2))

            # Llenamos de ceros la direccion
            if   slot == 0: 
                contexto.Dr0 = 0x00000000
            elif slot == 1: 
                contexto.Dr1 = 0x00000000
            elif slot == 2: 
                contexto.Dr2 = 0x00000000
            elif slot == 3: 
                contexto.Dr3 = 0x00000000

            # Removemos la bandera de condicion
            contexto.Dr7 &= ~(3 << ((slot * 4) + 16))

            # Removemos la bandera de longitud
            contexto.Dr7 &= ~(3 << ((slot * 4) + 18))

            # Reiniciamos el contexto del thread con el breakpoint removido
            h_thread = self.abrir_thread(thread_id)
            kernel32.SetThreadContext(h_thread,byref(contexto))
            
        # Removemos el breakpoint de la lista interna
        del self.hardware_breakpoints[slot]

        return True

    def breakpoint_establecer_memoria (self, address, size):
        
        mbi = MEMORY_BASIC_INFORMATION()
        
        # Intentamos descubrir la direccion base de la pagina de memoria
        if kernel32.VirtualQueryEx(self.h_process, address, byref(mbi), sizeof(mbi)) < sizeof(mbi):
            return False

    
        pagina_actual = mbi.BaseAddress
    
        # Establecemos los permisos en todas las paginas afectadas por nuestro breakpoint de memoria
        while pagina_actual <= address + size:
        
            # Agregamos la pagina a la lista, lo que diferenciara las paginas con guardia de aquellas que fueron establecidas
            # por el sistema operativo o el proceso siendo debuggeado
            self.guarded_pages.append(pagina_actual)
            
            proteccion_antigua = c_ulong(0)
            if not kernel32.VirtualProtectEx(self.h_process, pagina_actual, size, mbi.Protect | PAGE_GUARD, byref(proteccion_antigua)):
                return False
         
            # Incrementamos nuestro rango en la cantidad default del tamaño de la pagina de memoria del sistema
            pagina_actual += self.page_size
    
        # Agregamos el breakpoint de memoria a nuestra lista global
        self.memory_breakpoints[address] = (address, size, mbi)
    
        return True

db = debugger()
pid = input("Ingresa el PID del proceso al cual adjuntarse: ")
db.adjuntar(int(pid))
printf = db.resolucion_de_funciones("msvcrt.dll","printf")
print ("[*] Direccion de printf: 0x%08x" % printf)
db.breakpoint_set_hardware(printf,1,HW_EXECUTE)
db.ejecutar()