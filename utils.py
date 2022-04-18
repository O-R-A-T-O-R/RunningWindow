import getpass, os

def change_position(root_variable,x,y):
    root_variable.geometry('+{}+{}'.format(x,y))

def add_to_startup(file_path=""):
    USER_NAME = getpass.getuser()
    if not file_path:
        file_path = os.path.dirname(os.path.realpath(__file__)) + '\\main'

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

add_to_startup()