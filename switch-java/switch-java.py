import winreg

import ctypes
import os
import sys
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

    if not pathlib.Path(os.path.abspath(os.path.dirname(__file__)) + "\\config.json").is_file():
        print("No config file found. Ending program.")
        sys.exit()

    try:
        with open(pathlib.Path(os.path.abspath(os.path.dirname(__file__)) + "\\config.json"), "r",
                  encoding="utf-8") as config_file:
            config = json.load(config_file)
    except json.decoder.JSONDecodeError:
        print("Incorrect json format of config. Ending program.")
        sys.exit()

    target_type = str(input("\nEnter your Java type (jre or jdk): ")).lower()
    if target_type == "jre":
        target_version = str(input("Enter your Java version (" + str(config["jre_versions"][0].keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "") + "): ")).lower()
    elif target_type == "jdk":
        target_version = str(input("Enter your Java version (" + str(config["jdk_versions"][0].keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "") + "): ")).lower()
    else:
        print("Incorrect Java type (\"" + target_type + "\"): its should be \"jre\" or \"jdk\". Ending program.")
        sys.exit()

    if config["switch_mode"] == "user":
        if target_type == "jre":
            for java_version, path_to_java in config["jre_versions"][0].items():
                if java_version == target_version:
                    print("Run in " + config["switch_mode"] + " mode. Unable to set registry values to select Java version for execution when double-clicking a \".jar\" file")
                    os.system("REG delete \"HKEY_CURRENT_USER\Environment\" /F /V \"JAVA_HOME\"")
                    os.system("setx JRE_HOME \"" + path_to_java + "\"")
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

                                os.system("setx Path \"" + path_to_java + "\\bin;" + path + "\"")
                                print(
                                    "\nIf you have three success notifications above (or two and a \"Missing key error\"), Java (JRE) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                                    "\nYou must restart the CMD to test with \"java -version\".")
                                sys.exit()

                            i += 1
                    except WindowsError:
                        os.system("setx Path \"" + path_to_java + "\\bin;\"")
                        print(
                            "\nIf you have three success notifications above (or two and a \"Missing key error\"), Java (JRE) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                            "\nYou must restart the CMD to test with \"java -version\".")
                        sys.exit()

            print("No version of Java (JRE) provided in the config matches your request. Available versions are: " + str(config["jre_versions"][0].keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "\"") + ". Ending program.")
            sys.exit()

        else:
            for java_version, path_to_java in config["jdk_versions"][0].items():
                if java_version == target_version:
                    print("Run in " + config["switch_mode"] + " mode. Unable to set registry values to select Java version for execution when double-clicking a \".jar\" file")
                    os.system("setx JRE_HOME \"" + path_to_java + "\"")
                    os.system("setx JAVA_HOME \"" + path_to_java + "\"")
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

                                os.system("setx Path \"" + path_to_java + "\\bin;" + path + "\"")
                                print(
                                    "\nIf you have three success notifications above, Java (JDK) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                                    "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                                sys.exit()

                            i += 1
                    except WindowsError:
                        os.system("setx Path \"" + path_to_java + "\\bin;\"")
                        print(
                            "\nIf you have two success notifications above, Java (JDK) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                            "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                        sys.exit()

            print("No version of Java (JDK) provided in the config matches your request. Available versions are: " + str(config["jdk_versions"][0].keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "\"") + ". Ending program.")
            sys.exit()

    elif config["switch_mode"] == "system":
        if not ctypes.windll.shell32.IsUserAnAdmin() != 0:
            print("You must run in administrator mode to be able to run switch-java for the " + config["switch_mode"] + ".")
            sys.exit()

        if target_type == "jre":
            for java_version, path_to_java in config["jre_versions"][0].items():
                if java_version == target_version:
                    os.system("REG delete \"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /F /V \"JAVA_HOME\"")
                    os.system("REG add \"HKEY_CLASSES_ROOT\jarfile\shell\open\command\" /F /D \"\\\"" + path_to_java + "\\bin\\javaw.exe\\\" -jar \\\"%1\\\" %*\"")
                    os.system("REG add \"HKEY_CLASSES_ROOT\.jar\" /F /D \"jarfile\"")
                    os.system("setx -m JRE_HOME \"" + path_to_java + "\"")
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

                                os.system("setx -m Path \"" + path_to_java + "\\bin;" + path + "\"")
                                print(
                                    "\nIf you have three success notifications above (ore two and a \"Missing key error\"), Java (JRE) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                                    "\nYou must restart the CMD to test with \"java -version\".")
                                sys.exit()

                            i += 1
                    except WindowsError:
                        os.system("setx -m Path \"" + path_to_java + "\\bin;\"")
                        print(
                            "\nIf you have three success notifications above (ore two and a \"Missing key error\"), Java (JRE) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                            "\nYou must restart the CMD to test with \"java -version\".")
                        sys.exit()

            print(
                "No version of Java (JRE) provided in the config matches your request. Available versions are: " + str(config["jre_versions"][0].keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "\"") + ". Ending program.")
            sys.exit()

        else:
            for java_version, path_to_java in config["jdk_versions"][0].items():
                if java_version == target_version:
                    os.system("REG add \"HKEY_CLASSES_ROOT\jarfile\shell\open\command\" /F /D \"\\\"" + path_to_java + "\\bin\\javaw.exe\\\" -jar \\\"%1\\\" %*\"")
                    os.system("REG add \"HKEY_CLASSES_ROOT\.jar\" /F /D \"jarfile\"")
                    os.system("setx -m JRE_HOME \"" + path_to_java + "\"")
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
                                    if ("java" not in regKey_value.split(";")[i].lower() or "switch-java" in
                                        regKey_value.split(";")[i].lower()) \
                                            and "jdk" not in regKey_value.split(";")[i].lower() \
                                            and "openjdk" not in regKey_value.split(";")[i].lower() \
                                            and "jre" not in regKey_value.split(";")[i].lower() \
                                            and regKey_value.split(";")[i] != "":
                                        path += regKey_value.split(";")[i] + ";"

                                os.system("setx -m Path \"" + path_to_java + "\\bin;" + path + "\"")
                                print(
                                    "\nIf you have three success notifications above, Java (JDK) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                                    "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                                sys.exit()

                            i += 1
                    except WindowsError:
                        os.system("setx -m Path \"" + path_to_java + "\\bin;\"")
                        print(
                            "\nIf you have two success notifications above, Java (JDK) " + java_version + " is correctly set as " + config["switch_mode"] + " default."
                            "\nYou must restart the CMD to test with \"java -version\" for JRE or \"javac -version\" for JDK.")
                        sys.exit()

            print(
                "No version of Java (JDK) provided in the config matches your request. Available versions are: " + str(config["jdk_versions"][0].keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "\"") + ". Ending program.")
            sys.exit()

    else:
        print("Incorrect switch_mode: its should be \"user\" or \"system\". Ending program.")
        sys.exit()
