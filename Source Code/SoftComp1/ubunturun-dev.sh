#!/bin/bash
# Running the script needs Python3 well configured with pygame library.

cd ~/Desktop/simulation/PycharmProjects/bin

python3 ~/Desktop/simulation/PycharmProjects/SoftComp.py & python3
~/Desktop/simulation/PycharmProjects/gravity.py & python3
~/Desktop/simulation/PycharmProjects/interpolate.py & python3
~/Desktop/simulation/PycharmProjects/keyframes.py & python3
~/Desktop/simulation/PycharmProjects/obstacles.py & python3
~/Desktop/simulation/PycharmProjects/particles.py & python3
~/Desktop/simulation/PycharmProjects/PyIgnition.py & python3
~/Desktop/simulation/PycharmProjects/constants.py&
