# Group-13_Term_Project_2017_Soft_Computing
Soft Computing Term Project under the guidance of Prof. Sudhir Kumar Barai. 

The repository contains the source code that is a result of trying and simulating several mathematical models.

The current model mimics a vague decision making process of human mind which aim at reducing collision risks, optimizing time and energy to reach
the goal point.

Could be tested by running the corresponding bash scripts, and following the given instructions below:

Prerequisites:
Python 3.4 or higher
Python Libraries: PyGame and for creating particle dynamics we used PyIgnition which are basically codes available in the internet to mimic particle, obstacle motion easily.(PyIgnition is developed using PyGame) and related dependencies.

For Linux:
Bash Scripts files are maintained for different demo versions
Create a folder named bin in user’s home directory.
Place the Linux folder in the CD on Desktop renaming it to be simulation
Copy the contents of the bin directory in Linux folder to the bin directory in user’s home directory.
Make sure the user’s home directory is added to environment path variable
If not, add the line to bashrc system file: export PATH=~/bin:"$PATH"
Change the mode of the files copied to be executable
Go to terminal and type simurun1 for demo1, simurun2 for demo2, simurun3 for demo3 and simurun4 for demo4, simurun5 for demo5 and simurun6 for demo6 presentation respectively.

For Windows:
.exe compilations have been built for all the six demos although they are a bit unstable in some environments.
In the disc go to Windows->SoftComp1->dist->SoftComp1->SoftComp.exe for demo 1 and similar paths for other demos.
.exe compilations can be easily build using running pyinstaller on the Linux files in case that doesn’t seem to work.

Overview : 
There are in total six programs which shows the application of fuzzy logic in Intelligent-Path planning in various chaotic environments.
SoftComp1 runs for 10 dynamic obstacles.
SoftComp2 runs for 10 dynamic obstacles and a moving target and a target-seeking obstacle.
SoftComp3 runs for 25 dynamic obstacles.
SoftComp4 runs for 10 dynamic obstacles, one target and several target seeking particles.
SoftComp5 runs for 10 static obstacles of different sizes.
SoftComp6 runs for 10 dynamic obstacles where there are 5 pairs of target and target seeking particle.
Each program runs on 6 major python files.
           1. SoftComp.py
           2. PyIgnition.py
           3. particles.py
           4. obstacles.py
           5. keyframes.py
           6. constants.py

“SoftComp.py” imports “PyIgnition.py” which further imports all the other mentioned files.
“SoftComp.py” also imports “PyGame” library which is used to create the simulation window.And this provides the backend for creating the simulation completely and it’s used to run the code at 100 frames per second.
In each program “obstacle.py” is used to make randomly moving obstacles.
“particles.py”  is used to create the target seeking obstacles.
“keyframes.py”  is used to detect the mouse clicks which are used to specify the obstacles, particles and target.And it helps in running the codes in 100 frames per second.
“constants.py”  contains the variables which are globally used across all the 6 above mentioned files.
“particles.py”  contains the fuzzy logic code for the target seeking particle which uses the fuzzy logic to find its way to the target.
“SoftComp.py” contains the code for creating the simulation and creating effect classes for obstacles,particles and assigning different obstacles,particles with different mouse clicks.This file imports “obstacles.py” indirectly to get the features of the obstacles for creating the same.
