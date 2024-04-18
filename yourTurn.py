#! /usr/bin/python
#################################################################################################
# Author:
# Date:
# Description of Script:
#################################################################################################
import sys  
import threading  
import ipaddress  
import re 
from scapy.all import *  
import nmap  

# Set to store scanned hosts to avoid duplicate scans
scanned_hosts = set()  # Initialize an empty set to store scanned hosts
lock = threading.Lock()  # Create a lock to ensure thread-safe access to shared resources

def nmap_vulnerability_scan(host, tcp_ports=None):
    try:
        # Create Nmap PortScanner object
        nm = nmap.PortScanner()
        
        # Construct Nmap arguments based on TCP ports input
        nmap_args = '' # Fill out your arguments for your Nmap Scan right here
        if tcp_ports:
            nmap_args += f'-p {tcp_ports}'
        
        # Perform Nmap vulnerability scan on the specified host with optional TCP ports
        nm.scan(hosts=host, arguments=nmap_args)
        
        # Process and print vulnerability scan results
        for host in nm.all_hosts():
            print("Vulnerability Scan Results for Host:", host)
            # Check if there are any vulnerability scripts for the current host
            if 'scripts' in nm[host]:
                # Iterate over each vulnerability script result
                for script_id, script_output in nm[host]['scripts'].items():
                    print(f"Script ID: {script_id}")
                    print("Output:")
                    print(script_output)
            else:
                print("No vulnerability scripts found for this host.")
    except Exception as e:
        print(f"Error during vulnerability scan: {e}")

# Ask user for target IP address and TCP ports input
target_ip = input("Enter the target IP address: ")
tcp_ports_input = input("Enter TCP ports to scan (e.g., 22-25,80,443): ")

# Example usage with user input
nmap_vulnerability_scan(target_ip, tcp_ports_input)

# Your Turn!
# Reference the net_terrorizer.py file or use google fu to determine how to configure the rest of your script.
