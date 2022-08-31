# Switch java

## Presentation

This project is a small tool aimed at making it easy to use different versions of java on a single computer without digging into environment variables.

This project was created to work under windows. It will not work on other OS as it works with Windows registry keys

## How to use

### Setup

Using switch-java is very simple. Start by downloading the version that suits you in the [release tab](https://github.com/Disk-MTH/Switch-java/releases). You have the choice to have an embedded python environment or not. If you already have a python 3 on your system, it's not useful.


Warning, the installation must include the console launcher (To check type the "windows" key, then type "cmd" in the search window and press "enter". Once there 'command prompt launched, type "python", type "enter" and if python launches in 'command prompt, then it's good),

Once the desired version is downloaded, unzip it, and modify the "[config.json](https://github.com/Disk-MTH/Switch-java/blob/master/switch-java/config.json)" file (respect [json format](https://www.json.org/json-en.html)):

- switch_mode: Don't touch it yet. It will be automatically defined during setup. On the other hand, you can modify it later in order to change the mode of change java.


- jre_versions: List all your java JRE version. The version identifier will be the one to type when you want to change Java and the associated value is the path to the installation of the Java version. /!\ Path separator must be "\\\\" or "/" but not "\\" | if you doesn't have JRE leave braces empty /!\


- jdk_versions: List all your java JDK version. The version identifier will be the one to type when you want to change Java and the associated value is the path to the installation of the Java version. /!\ Path separator must be "\\\\" or "/" but not "\\" | if you doesn't have JDK leave braces empty /!\


Once your configuration is done, run the "[setup.bat](https://github.com/Disk-MTH/Switch-java/blob/master/switch-java/setup/setup.bat)" script by double-click on it (for "user" mode) or by right-click and selecting "Run as administrator" (for "system" mode). This script will automatically "install" the program either in "C:\Users\your_user\switch-java" for the "user" mode or in "C:\Program Files\switch-java" for the "system" mode.

You can change the configuration at any time by going to the installation folder and modifying the "[config.json](https://github.com/Disk-MTH/Switch-java/blob/master/switch-java/config.json)" file.

You can now delete the folder (as well as the zip) of your downloads, it will no longer be useful.

### Clear Java

If you have already defined environment variables for Java, you can automatically remove them thanks to a provided script. Open a command prompt (normal for "user" mode and administrator for "system" mode) and run the following command: ``clear-java`` and enter your mode ("user" or "system").

### Switch Java

To switch version of Java, you must execute the command ``switch-java`` in a command prompt (normal for "user" mode and administrator for "system" mode), then give your switch mode ("user" or "system"), then your type of Java ("jre" or "jdk") and finally give the version to define (the list of available versions will be given to you in the console and it corresponds to that defined in the config).

/!\ "user" mode does not allow setting registry key values to select which java version to run when double-clicking a ".jar" file. It's a limitation of windows and as far as I know, I can't change it.

### Uninstall

If you don't have it/no longer download the zip of the latest release (with embedded python or not), unzip it, and run the "uninstall.bat" script by double-click on it (for "user" mode) or by right-click and selecting "Run as administrator" (for "system" mode).

## License

All the files in this repository are completely free of rights (see the [license](https://github.com/Disk-MTH/Switch-java/blob/master/license.txt)) so 
you can grab the images, the code ... and do whatever you want with them (just 
respect the [license](https://github.com/Disk-MTH/Switch-java/blob/master/license.txt)).

Thanks for reading and good development!

Disk_MTH