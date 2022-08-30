import winreg
import os
import sys
import json
import pathlib
import re
import subprocess

if __name__ == '__main__':
    global config

    print("#####################################################################")
    print("#      #  ___    _        _           __  __   _____   _  _  #      #")
    print("#      # |   \  (_)  ___ | |__       |  \/  | |_   _| | || | #      #")
    print("#      # | |) | | | (_-< | / /       | |\/| |   | |   | __ | #      #")
    print("#      # |___/  |_| /__/ |_\_\  ___  |_|  |_|   |_|   |_||_| #      #")
    print("#      #                       |___|                         #      #")
    print("# Created by Disk_MTH. Look https://github.com/Disk-MTH/Switch-java #")
    print("#####################################################################")

    if len(sys.argv) < 2:
        print("No java version specified as argument. Ending program.")
        sys.exit()
    elif not pathlib.Path(os.path.abspath(os.path.dirname(__file__)) + "\\config.json").is_file():
        print("No config file found. Ending program.")
        sys.exit()

    try:
        with open(pathlib.Path(os.path.abspath(os.path.dirname(__file__)) + "\\config.json"), "r",
                  encoding="utf-8") as config_file:
            config = json.load(config_file)
    except json.decoder.JSONDecodeError:
        print("Incorrect json format of config. Ending program.")
        sys.exit()

    if config["switch_mode"] == "user":
        for java_version, path_to_java in config["java_versions"][0].items():
            if java_version == sys.argv[1]:
                os.system("setx JAVA_HOME \"" + path_to_java + "\"")
                try:
                    i = 0
                    while True:
                        regKey_name, regKey_value, regKey_type = winreg.EnumValue(winreg.OpenKey(
                            winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), "Environment"), i)

                        if regKey_name.lower() == "path":
                            path = ""
                            for i in range(len(regKey_value.split(";"))):
                                if ("java" not in regKey_value.split(";")[i].lower() or "switch-java" in regKey_value.split(";")[i].lower()) \
                                        and "jdk" not in regKey_value.split(";")[i].lower() \
                                        and "openjdk" not in regKey_value.split(";")[i].lower() \
                                        and "jre" not in regKey_value.split(";")[i].lower() \
                                        and regKey_value.split(";")[i] != "":
                                    path += regKey_value.split(";")[i] + ";"

                            os.system("setx Path \"" + path_to_java + "\\bin;" + path + "\"")
                            print("\nIf you have two success notifications above, then Java " + java_version + " is correctly set as user default. "
                                  "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                            sys.exit()

                        i += 1
                except WindowsError:
                    os.system("setx Path \"" + path_to_java + "\\bin;")
                    print("\nIf you have two success notifications above, then Java " + java_version + " is correctly set as user default. "
                          "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                    sys.exit()

        print("No version of java provided in the config matches your request. Ending program.")
        sys.exit()

    elif config["switch_mode"] == "system":
        for java_version, path_to_java in config["java_versions"][0].items():
            if java_version == sys.argv[1]:
                os.system("setx -m JAVA_HOME \"" + path_to_java + "\"")
                try:
                    i = 0
                    while True:
                        regKey_name, regKey_value, regKey_type = winreg.EnumValue(winreg.OpenKey(
                            winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE),
                            "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment"), i)

                        if regKey_name.lower() == "path":
                            path = ""
                            for i in range(len(regKey_value.split(";"))):
                                if ("java" not in regKey_value.split(";")[i].lower() or "switch-java" in regKey_value.split(";")[i].lower()) \
                                        and "jdk" not in regKey_value.split(";")[i].lower() \
                                        and "openjdk" not in regKey_value.split(";")[i].lower() \
                                        and "jre" not in regKey_value.split(";")[i].lower() \
                                        and regKey_value.split(";")[i] != "":
                                    path += regKey_value.split(";")[i] + ";"

                            os.system("setx -m Path \"" + path_to_java + "\\bin;" + path + "\"")
                            print(
                                "\nIf you have two success notifications above, then Java " + java_version + " is correctly set as user default. "
                                "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                            sys.exit()

                        i += 1
                except WindowsError:
                    os.system("setx -m Path \"" + path_to_java + "\\bin;")
                    print(
                        "\nIf you have two success notifications above, then Java " + java_version + " is correctly set as user default. "
                        "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                    sys.exit()

        print("No version of java provided in the config matches your request. Ending program.")
        sys.exit()

    else:
        print("Incorrect switch_mode: its should be \"user\" or \"system\". Ending program.")
        sys.exit()
