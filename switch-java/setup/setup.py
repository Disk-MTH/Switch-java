import winreg

import ctypes
import os
import sys
import shutil
import json
import pathlib

if __name__ == '__main__':
    print("#####################################################################")
    print("#      #  ___    _        _           __  __   _____   _  _  #      #")
    print("#      # |   \  (_)  ___ | |__       |  \/  | |_   _| | || | #      #")
    print("#      # | |) | | | (_-< | / /       | |\/| |   | |   | __ | #      #")
    print("#      # |___/  |_| /__/ |_\_\  ___  |_|  |_|   |_|   |_||_| #      #")
    print("#      #                       |___|                         #      #")
    print("# Created by Disk_MTH. Look https://github.com/Disk-MTH/Switch-java #")
    print("#####################################################################")

    setup_mode = str(input("\nEnter your setup mode (user or system): ")).lower()

    if setup_mode == "user":
        print("\"Switch-java\" files will be stored in: " + os.environ["USERPROFILE"] + "\\switch-java")
        if os.path.isdir(os.environ["USERPROFILE"] + "\\switch-java"):
            print("A \"switch-java\" folder already exists. Removal in progress.")
            shutil.rmtree(os.environ["USERPROFILE"] + "\\switch-java")
            print("End of deletion of \"switch-java\" folder.")

        print("Started copying \"switch-java\" files. It may take a while if you are using bundled python.")
        shutil.copytree(pathlib.Path(os.path.abspath(os.path.dirname(__file__)).replace("setup", "")), os.environ["USERPROFILE"] + "\\switch-java")
        shutil.rmtree(os.environ["USERPROFILE"] + "\\switch-java\\setup")
        shutil.rmtree(os.environ["USERPROFILE"] + "\\switch-java\\uninstall")
        print("End of copying \"switch-java\" files")

        with open(os.environ["USERPROFILE"] + "\\switch-java\\config.json", "r+", encoding="utf-8") as config_file:
            content = json.load(config_file)
            content["switch_mode"] = setup_mode
            config_file.truncate(0)
            config_file.seek(0)
            json.dump(content, config_file, indent=4)
        print("End of config setup.")

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

                    os.system("setx Path \"" + os.environ["USERPROFILE"] + "\\switch-java;" + os.environ["USERPROFILE"] + "\\switch-java\\clear-java;" + path + "\"")
                    print("\nIf you have a success notification above, \"Switch-java\" is correctly setup for " + setup_mode + ".")
                    os.system("pause")
                    sys.exit()

                i += 1
        except WindowsError:
            os.system("setx Path \"" + os.environ["USERPROFILE"] + "\\switch-java;" + os.environ["USERPROFILE"] + "\\switch-java\\clear-java;\"")
            print("\nIf you have a success notification above, \"Switch-java\" is correctly setup for " + setup_mode + ".")
            os.system("pause")
            sys.exit()

    elif setup_mode == "system":
        if not ctypes.windll.shell32.IsUserAnAdmin() != 0:
            print("You must run in administrator mode to be able to setup switch-java for the " + setup_mode + ".")
            os.system("pause")
            sys.exit()

        print("\"Switch-java\" files will be stored in: " + os.environ["PROGRAMFILES"] + "\\switch-java")
        if os.path.isdir(os.environ["PROGRAMFILES"] + "\\switch-java"):
            print("A \"switch-java\" folder already exists. Removal in progress.")
            shutil.rmtree(os.environ["PROGRAMFILES"] + "\\switch-java")
            print("End of deletion of \"switch-java\" folder.")

        print("Started copying \"switch-java\" files. It may take a while if you are using bundled python.")
        shutil.copytree(pathlib.Path(os.path.abspath(os.path.dirname(__file__)).replace("setup", "")),
                        os.environ["PROGRAMFILES"] + "\\switch-java")
        shutil.rmtree(os.environ["PROGRAMFILES"] + "\\switch-java\\setup")
        shutil.rmtree(os.environ["PROGRAMFILES"] + "\\switch-java\\uninstall")
        print("End of copying \"switch-java\" files")

        with open(os.environ["PROGRAMFILES"] + "\\switch-java\\config.json", "r+", encoding="utf-8") as config_file:
            content = json.load(config_file)
            content["switch_mode"] = setup_mode
            config_file.truncate(0)
            config_file.seek(0)
            json.dump(content, config_file, indent=4)
        print("End of config setup.")

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

                    os.system("setx -m Path \"" + os.environ["PROGRAMFILES"] + "\\switch-java;" + os.environ["PROGRAMFILES"] + "\\switch-java\\clear-java;" + path + "\"")
                    print("\nIf you have a success notification above, \"Switch-java\" is correctly setup for " + setup_mode + ".")
                    os.system("pause")
                    sys.exit()

                i += 1
        except WindowsError:
            os.system("setx -m Path \"" + os.environ["PROGRAMFILES"] + "\\switch-java;" + os.environ["PROGRAMFILES"] + "\\switch-java\\clear-java;\"")
            print("\nIf you have a success notification above, \"Switch-java\" is correctly setup for " + setup_mode + ".")
            os.system("pause")
            sys.exit()

    else:
        print("Incorrect setup mode (\"" + setup_mode + "\"): its should be \"user\" or \"system\". Ending program.")
        os.system("pause")
        sys.exit()
