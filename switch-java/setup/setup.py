import winreg
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

    if len(sys.argv) < 2:
        print("No setup profile specified as argument. Ending program.")
        sys.exit()

    if sys.argv[1] != "user":
        pass
    elif sys.argv[1] != "system":
        pass
    else:
        print("Incorrect setup profile: its should be \"user\" or \"system\". Ending program.")
        sys.exit()
