import nmap

def nmap_vulnerability_scan(host):
    try:
        # Create Nmap PortScanner object
        nm = nmap.PortScanner()
        # Perform Nmap vulnerability scan on the specified host
        nm.scan(hosts=host, arguments='-T4 -sS -sV -O --version-all --script=banner -A --script vulners')
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

# Example usage
nmap_vulnerability_scan("your_target_host_or_ip")
