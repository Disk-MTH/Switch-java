import winreg

import ctypes
import os
import sys
import shutil

if __name__ == '__main__':
    print("#####################################################################")
    print("#      #  ___    _        _           __  __   _____   _  _  #      #")
    print("#      # |   \  (_)  ___ | |__       |  \/  | |_   _| | || | #      #")
    print("#      # | |) | | | (_-< | / /       | |\/| |   | |   | __ | #      #")
    print("#      # |___/  |_| /__/ |_\_\  ___  |_|  |_|   |_|   |_||_| #      #")
    print("#      #                       |___|                         #      #")
    print("# Created by Disk_MTH. Look https://github.com/Disk-MTH/Switch-java #")
    print("#####################################################################")

    uninstall_mode = str(input("\nEnter your setup mode (user or system): ")).lower()

    if uninstall_mode == "user":
        if os.path.isdir(os.environ["USERPROFILE"] + "\\switch-java"):
            print("A \"switch-java\" has been found. Removal in progress.")
            shutil.rmtree(os.environ["USERPROFILE"] + "\\switch-java")
            print("End of deletion of \"switch-java\" folder.")
        else:
            print("No \"switch-java\" folder found for current " + uninstall_mode + ". Ending program.")

        try:
            i = 0
            while True:
                regKey_name, regKey_value, regKey_type = winreg.EnumValue(winreg.OpenKey(
                    winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Environment"), i)

                if regKey_name.lower() == "path":
                    path = ""
                    for i in range(len(regKey_value.split(";"))):
                        if "switch-java" not in regKey_value.split(";")[i].lower() and regKey_value.split(";")[i] != "":
                            path += regKey_value.split(";")[i] + ";"

                    if path == "":
                        os.system("REG delete \"HKCU\Environment\" /F /V \"Path\"")
                    else:
                        os.system("setx Path \"" + path + "\"")
                    print("\nIf you have a success notification above, \"Switch-java\" is correctly uninstalled for " + uninstall_mode + ".")
                    os.system("pause")
                    sys.exit()

                i += 1
        except WindowsError:
            print("No environment variables to remove for " + uninstall_mode + ". Ending program.")
            os.system("pause")
            sys.exit()

    elif uninstall_mode == "system":
        if not ctypes.windll.shell32.IsUserAnAdmin() != 0:
            print("You must run in administrator mode to be able to setup switch-java for the " + uninstall_mode)
            os.system("pause")
            sys.exit()

        if os.path.isdir(os.environ["PROGRAMFILES"] + "\\switch-java"):
            print("A \"switch-java\" has been found. Removal in progress.")
            shutil.rmtree(os.environ["PROGRAMFILES"] + "\\switch-java")
            print("End of deletion of \"switch-java\" folder.")
        else:
            print("No \"switch-java\" folder found for current " + uninstall_mode + ". Ending program.")

        try:
            i = 0
            while True:
                regKey_name, regKey_value, regKey_type = winreg.EnumValue(winreg.OpenKey(
                    winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE),
                    "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment"), i)

                if regKey_name.lower() == "path":
                    path = ""
                    for i in range(len(regKey_value.split(";"))):
                        if "switch-java" not in regKey_value.split(";")[i].lower() and regKey_value.split(";")[i] != "":
                            path += regKey_value.split(";")[i] + ";"

                    if path == "":
                        os.system("REG delete \"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /F /V \"Path\"")
                    else:
                        os.system("setx -m Path \"" + path + "\"")
                    print("\nIf you have a success notification above, \"Switch-java\" is correctly uninstalled for " + uninstall_mode + ".")
                    os.system("pause")
                    sys.exit()

                i += 1
        except WindowsError:
            print("No environment variables to remove for " + uninstall_mode + ". Ending program.")
            os.system("pause")
            sys.exit()

    else:
        print("Incorrect uninstall mode (\"" + uninstall_mode + "\"): its should be \"user\" or \"system\". Ending program.")
        os.system("pause")
        sys.exit()
