import getpass, os

def add_to_startup(exe_file= ""):
    USER_NAME = getpass.getuser()

    file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

    if not exe_file:
        for elem in os.listdir(file_path):
            file_name, extension = elem.split('.')

            if extension == 'exe':
                exe_file = elem
                break

    with open(os.path.join(bat_path, "open.bat"), "w+") as bat_file:
        exe_path = os.path.join(file_path, exe_file)

        bat_file.write(f'start {exe_path}')