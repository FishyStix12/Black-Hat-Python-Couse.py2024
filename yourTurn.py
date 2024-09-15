#! /usr/bin/python
#################################################################################################
# Author:
# Date:
# Description of Script:
#################################################################################################
import subprocess
import sys
import re
import ipaddress

def prompt_for_scripts():
    # Your turn

    # Ask the user for each script
    for script, description in script_descriptions.items():
        user_input = input(f"Do you want to use the {script} script? ({description}) [y/N]: ").lower()
        if user_input == 'y':
            scripts.append(script)
    
    return ','.join(scripts) if scripts else None

def nmap_scan(host, port_range):
    try:
        # Get the scripts the user wants to use
        selected_scripts = prompt_for_scripts()

        # Define the Nmap scan arguments based on the port range and selected scripts
        if port_range:
            # Your turn
def main():
    try:
        # Prompt user for input: list of remote IP addresses or CIDR notations
        remote_input = input("Enter the list of remote IP addresses or CIDR notations to scan (press Enter to exit): ").split()
        # Your Turn
