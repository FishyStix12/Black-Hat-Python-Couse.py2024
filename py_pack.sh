#!/bin/bash
#################################################################################################
# Author: Nicholas Fisher
# Date: April 2th 2024
# Description of Script
# Installs the necessary python packages for the BLack Hat Python Course. Please use
# "chmod +x py_pack.sh" to give the script execute permissions. Then type
# "./py_pack.sh" to run the script to install the necassary scripts on your linux instance.
#################################################################################################
sudo apt-get update
pip install python-nmap
pip install scapy
