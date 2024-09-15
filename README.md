# CharCyCon/UAH Delta Chi 2024: Black Hat Python <br />
# By: Nicholas Fisher <br /> 

![image](https://github.com/FishyStix12/BH.py-CharCyCon2024/assets/102126354/789f42ac-1c0f-46c3-b3d0-e023e83c6c0c) <br />
**Welcome to the Black Hat Python Course Delta Chi/For CharCyCon 2024!** <br />

**The file below is the PowerPoint used in the course:** <br />
For CharCyCon: <br />
Black Hat Python Course.pptx <br />

For Delta Chi <br />
DChi Black Hat Python Course.pptx <br />

**To set up the class environment please downdload and run the script below in your Linux instance:** <br />
1. course-repo-conf.sh - Sets up the Course Environment in Kali Linux for the CharCyCon 2024 Black Hat Python Course. <br />

# Exploring Network Security with Python and Nmap <br />
![image](https://github.com/FishyStix12/BH.py-CharCyCon2024/assets/102126354/76ab306e-4086-4a48-86f7-b0efc97be95d) <br />
**The Script below is the script we will be analyzing in the first part of the course:**
1. darknet_recon.py - The script provided is a Python tool for conducting network scans using Nmap and searching for Metasploit modules corresponding to identified vulnerabilities. It prompts the user to input remote IP addresses or CIDR notations for scanning. After performing Nmap scans to discover hosts and their open ports along with potential vulnerabilities, the script simulates finding CVE IDs. It then utilizes Metasploit's `msfconsole` command-line tool to search for exploit modules related to the identified CVEs. The user is prompted to enter the superuser password when required for executing commands. Overall, this script serves as a versatile tool for network reconnaissance and vulnerability assessment, seamlessly integrating Nmap and Metasploit functionalities. <br />
2. dark_wizard_gui.py - **Important Note: Please use this script as a superuser for it to work, and know that if you leave the port field blank it will do a full port scan, and will take time to load!** This Python script creates a graphical user interface (GUI) application named "Dark Net Wizard" using Tkinter. The application allows users to perform Nmap scans with firewall evasion techniques on specified target IP addresses or CIDR ranges. It includes options for inputting target ports or port ranges, and it displays the scan results, including any found Common Vulnerabilities and Exposures (CVEs) and Metasploit exploit modules if they exist. The GUI features a dark purple background color, an image display at the top (which can be replaced with a custom image link), input fields for IP addresses and ports, buttons for scanning and exiting the application, and an output box for displaying scan results and messages. <br />
3. net_terrorizer.py - This Python script offers a flexible solution for performing targeted Nmap network scans, allowing users to customize their scanning process through interactive prompts. Users can input a list of remote IP addresses or CIDR notations, along with a specific port range or a full port scan. The script guides users through selecting various Nmap scripts—each with a brief description of its functionality—such as detecting honeypots, analyzing firewall rules, or enumerating services and vulnerabilities. After constructing the Nmap command with the selected options, the script executes the scan and provides detailed results, including any identified CVEs and Metasploit modules. Users are given the option to save these results to a user-specified text file, enhancing the script's utility for comprehensive network analysis and documentation. This approach ensures that users can tailor their scans to specific needs while maintaining a detailed record of the scan outcomes. <br />

**Example outputs of some of the scripts and the gui!** <br />
1. dark_wizard_gui.py gui: <br />
 ![image](https://github.com/FishyStix12/WHPython_v1.02/assets/102126354/e91027d1-d1d7-4e23-b818-b7ea187cc533) <br />
2. darknet_recon.py output: <br />
   Enter the remote IP address or CIDR notation to scan (press Enter to exit): 192.168.1.0/24 <br />
   Nmap scan results for host: 192.168.1.1 <br />
   Host: 192.168.1.1 <br />
   Protocol: tcp <br />
   Port: 22    State: open    Service: ssh    Product: OpenSSH    Version: 7.6p1 Ubuntu    Extra Info: protocol 2.0 <br />
   Port: 80    State: open    Service: http    Product: nginx    Version: 1.14.0    Extra Info: (Ubuntu) <br />

   Metasploit modules for the found vulnerabilities: <br />

   Vulnerability: CVE-2017-1001000 <br />
   No Metasploit modules found for vulnerability: CVE-2017-1001000 <br />

   Vulnerability: CVE-2019-6977 <br />
   Module: exploit/linux/http/paloalto_traps_unauth_rce (Linux) <br />

   Vulnerability: CVE-2018-1000861 <br />
   No Metasploit modules found for vulnerability: CVE-2018-1000861 <br />

**Now it's your turn! Please use the scripts below to start the development of your very own nmap python tool!** <br />
1. py_pack.sh - Installs the necessary python packages for the BLack Hat Python Course. Please use "chmod +x py_pack.sh" to give the script execute permissions. Then type "./py_pack.sh" to run the script to install the necassary scripts on your linux instance. So you can properly test your scripts. <br />
2. yourTurn.py - Now it is your turn to create a Python tool designed for conducting network scans using the Nmap utility. It is intended to enhance scanning capabilities by incorporating techniques to avoid detection by firewalls, thereby increasing the accuracy and stealthiness of the scans. The script allows users to specify a target host or range of hosts, along with optional port ranges for scanning. It leverages subprocesses to execute Nmap commands and parse the resulting scan data, including information about open ports, services, operating systems, vulnerabilities (CVEs), and Metasploit modules. The script's modular design facilitates further customization and integration with other security tools or scripts, making it a versatile asset for network administrators and security professionals. <br />
