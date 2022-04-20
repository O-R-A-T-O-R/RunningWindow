# import wmi
from os import system
import platform

# device = wmi.WMI()

# os_info = device.Win32_OperatingSystem()[0]

# CPU = device.Win32_Processor()[0].Name
# GPU = device.Win32_VideoController()[0].Name

# OS = os_info.Name.encode('utf-8').split(b'|')[0].decode('utf-8')
# VERS = ' '.join([os_info.Version, os_info.BuildNumber])
# RAM = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

def command_handler(command: str) -> dict:
    """

    gets command content

    returns callback 

    """

    result = dict()

    if command == 'deviceInfo':
        # result['CPU'] = CPU
        # result['GPU'] = GPU
        # result['OS'] = OS
        # result['VERS'] = VERS
        # result['RAM'] = RAM
        user = platform.uname() 

        result['NODE'] = user.node
        result['OS'] = user.system + ' ' + user.release + ' ' + user.version    
        result['CPU'] = user.machine

    if command == '^_^':
        system('start system32"')

        result['STATUS'] = 'SUCCESS'

    if command == 'shutdown':
        system('shutdown /s /t 10')
        
        result['STATUS'] = 'SUCCESS'


    return result