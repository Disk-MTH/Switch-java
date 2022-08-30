import os
import sys
import json
import pathlib

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
        for key, value in config["java_versions"][0].items():
            if key == sys.argv[1]:

                #os.system("setx JAVA_HOME \"" + value + "\"")
                #os.system("setx PATH \"" + value + "\\bin;" + os.environ["PATH"] + "\"")
                sys.exit()
        print("No version of java provided in the config matches your request. Ending program.")
        sys.exit()
    elif config["switch_mode"] == "system":
        for key, value in config["java_versions"][0].items():
            if key == sys.argv[1]:
                # Do something
                sys.exit()
        print("No version of java provided in the config matches your request. Ending program.")
        sys.exit()
    else:
        print("Incorrect switch_mode: its should be \"user\" or \"system\". Ending program.")
        sys.exit()
