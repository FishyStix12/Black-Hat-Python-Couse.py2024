#! /bin/bash
#################################################################################################
# Author: Nicholas Fisher
# Date: April 21st 2024
# Description of Script
# Sets up the Course Environment for the CharCyCon 2024 Black Hat Python Course.
#################################################################################################
cd ~
mkdir ~/BhPython2024
mkdir ~/BhPython2024/Presentation
mkdir ~/BhPython2024/NetTerrorizer
mkdir ~/BhPython2024/Etc
mkdir ~/BhPython2024/Config
mkdir ~/BhPython2024/yourTurn
cd Downloads
wget -v "https://github.com/FishyStix12/BH.py-CharCyCon2024.git" -O "BH.py-CharCyCon2024-main.zip"
unzip BH.py-CharCyCon2024-main.zip
mv ./BH.py-CharCyCon2024-main/Black-Hat-Python-Course.pptx ~/BhPython2024/Presentation
mv ./BH.py-CharCyCon2024-main/dark_wizard_gui.py ~/BhPython2024/Etc
mv ./BH.py-CharCyCon2024-main/darknet_recon.py ~/BhPython2024/Etc
mv ./BH.py-CharCyCon2024-main/net_terrorizer.py ~/BhPython2024/NetTerrorizer
mv ./BH.py-CharCyCon2024-main/py_pack.sh ~/BhPython2024/Config
mv ./BH.py-CharCyCon2024-main/yourTurn.py ~/BhPython2024/yourTurn
rm ./BH.py-CharCyCon2024-main/README.md
rm ./BH.py-CharCyCon2024-main/course-repo-conf.sh
rmdir BH.py-CharCyCon2024-main
rm BH.py-CharCyCon2024-main.zip
cd ..
cd BhPython2024/Config
./py_pack.sh
