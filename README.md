# Pysubstitute

This project does not require any administrator permission, either for the setup 
of the environment or for the build of the project. So you can use this project 
on any windows computer. (If you are ever asked for permissions open an 
issue so I can see what this is due to)


## Presentation

This project is a small tool that allows you to simply replace a string of characters by another recursively in a folder.


## How to use and edit?

This project is completely self-contained: you don't need to have python installed, 
or anything else!

**__/!\ WARNING :__**

If during one of the following steps a SmartScreen window opens saying 
"SmartScreen has protected your computer", this is normal: the .exe files (which I made 
entirely myself) do not have a digital signature therefore windows defender is in panic. 
(If ever you do not trust my scripts do not go further because you will necessarily 
need them! Moreover you can see their "contents" in the "[uncompiled scripts](https://github.com/Disk-MTH/Pysubstitute/tree/master/scripts/uncompiled%20scripts)" folder).

Once the environment is setup (see below), it will take VERY long to move the folder, 
so choose a "permanent" location!


### Use:

Just download the latest [release](https://github.com/Disk-MTH/Pysubstitute/releases) available and run it. You don't have to do anything more than read what is written in the GUI!


### Edit:

1) Download:

To start, above the frame containing the code, there is a green button titled "Code", 
click on it, then on "Download ZIP" (or use [this link](https://github.com/Disk-MTH/Pysubstitute/archive/refs/heads/master.zip)). This will download you a .zip 
folder which you will need to extract (I recommend extracting to a "permanet" location). 

2) Setup:

(Warning : This step can be very long (depends on your computer))

Then in the unzipped folder find the "[scripts](https://github.com/Disk-MTH/Pysubstitute/tree/master/scripts)" folder and run the "setup.exe" 
file. This will open a window of the control terminal in which you will be able to 
follow the decompilation of the integrated python interpreter. (If you go back to 
the root folder of the project you can find a "python" folder that has been 
created).

/!\ : In case of update, if you resetup the python environment, it will overwrite the old 
one

3) Run:

To launch the application you simply need to run the "run.exe" file that you may have 
seen in the "[scripts](https://github.com/Disk-MTH/Pysubstitute/tree/master/scripts)" folder.

4) Edit:

You can modify the code of the application which is in the ".py" files in the [diskmth](https://github.com/Disk-MTH/Pysubstitute/tree/master/diskmth) folder to improve it.

5) Build:

To compile the program, nothing could be easier: all you have to do is run the 
"build.exe" file and a control terminal window will open. Wait for the end of the 
execution (when the terminal displays "press a key to continue ...") and you will see in 
the main folder a "build" folder in which 2 folders and 1 file will be present. go to the 
"dist" folder and you will have your compiled application. (If there is no icon or if the 
images do not all work, check the name of your images and restart a compilation. If 
that still does not work open an issue).

/!\ : If you ever rebuild the program after making changes, the program will overwrite 
the old build files.


## License

All the files in this repository are completely free of rights (see the [license](https://github.com/Disk-MTH/Pysubstitute/blob/master/license.txt)) so 
you can grab the images, the code ... and do whatever you want with them (just 
respect the [license](https://github.com/Disk-MTH/Pysubstitute/blob/master/license.txt)).

Thanks for reading and good development!

Disk_MTH