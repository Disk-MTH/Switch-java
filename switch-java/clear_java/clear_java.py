import winreg

import ctypes
import os
import sys

if __name__ == '__main__':
    print("#####################################################################")
    print("#      #  ___    _        _           __  __   _____   _  _  #      #")
    print("#      # |   \  (_)  ___ | |__       |  \/  | |_   _| | || | #      #")
    print("#      # | |) | | | (_-< | / /       | |\/| |   | |   | __ | #      #")
    print("#      # |___/  |_| /__/ |_\_\  ___  |_|  |_|   |_|   |_||_| #      #")
    print("#      #                       |___|                         #      #")
    print("# Created by Disk_MTH. Look https://github.com/Disk-MTH/Switch-java #")
    print("#####################################################################")

    clear_java_mode = str(input("\nEnter your setup mode (user or system): ")).lower()

    if clear_java_mode == "user":
        os.system("REG delete \"HKCU\Environment\" /F /V \"JRE_HOME\"")
        os.system("REG delete \"HKCU\Environment\" /F /V \"JAVA_HOME\"")

        try:
            i = 0
            while True:
                regKey_name, regKey_value, regKey_type = winreg.EnumValue(winreg.OpenKey(
                    winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Environment"), i)

                if regKey_name.lower() == "path":
                    path = ""
                    for i in range(len(regKey_value.split(";"))):
                        if ("java" not in regKey_value.split(";")[i].lower() or "switch-java" in
                            regKey_value.split(";")[i].lower()) \
                                and "jdk" not in regKey_value.split(";")[i].lower() \
                                and "openjdk" not in regKey_value.split(";")[i].lower() \
                                and "jre" not in regKey_value.split(";")[i].lower() \
                                and regKey_value.split(";")[i] != "":
                            path += regKey_value.split(";")[i] + ";"

                    if path == "":
                        os.system("REG delete \"HKCU\Environment\" /F /V \"Path\"")
                    else:
                        os.system("setx Path \"" + path + "\"")
                    print("\nIf you have success notification above (or \"Missing key error\"), Java is correctly removed from " + clear_java_mode + " environment.")
                    sys.exit()

                i += 1
        except WindowsError:
            print("\nIf you have success notification above (or \"Missing key error\"), Java is correctly removed from " + clear_java_mode + " environment.")
            sys.exit()

    elif clear_java_mode == "system":
        if not ctypes.windll.shell32.IsUserAnAdmin() != 0:
            print("You must run in administrator mode to be able to setup switch-java for the " + clear_java_mode + ".")
            sys.exit()

        os.system("REG delete \"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /F /V \"JRE_HOME\"")
        os.system("REG delete \"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /F /V \"JAVA_HOME\"")

        try:
            i = 0
            while True:
                regKey_name, regKey_value, regKey_type = winreg.EnumValue(winreg.OpenKey(
                    winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE),
                    "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment"), i)

                if regKey_name.lower() == "path":
                    path = ""
                    for i in range(len(regKey_value.split(";"))):
                        if ("java" not in regKey_value.split(";")[i].lower() or "switch-java" in
                            regKey_value.split(";")[i].lower()) \
                                and "jdk" not in regKey_value.split(";")[i].lower() \
                                and "openjdk" not in regKey_value.split(";")[i].lower() \
                                and "jre" not in regKey_value.split(";")[i].lower() \
                                and regKey_value.split(";")[i] != "":
                            path += regKey_value.split(";")[i] + ";"

                    if path == "":
                        os.system("REG delete \"HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /F /V \"Path\"")
                    else:
                        os.system("setx -m Path \"" + path + "\"")
                    print("\nIf you have success notification above (or \"Missing key error\"), Java is correctly removed from " + clear_java_mode + " environment.")
                    sys.exit()

                i += 1
        except WindowsError:
            print("\nIf you have success notification above (or \"Missing key error\"), Java is correctly removed from " + clear_java_mode + " environment.")
            sys.exit()

    else:
        print("Incorrect clear Java mode (\"" + clear_java_mode + "\"): its should be \"user\" or \"system\". Ending program.")
        sys.exit()
