# Fuel-1.4.1-RCE-Updated
- Update to CVE-2018-16763
- Exploit Title: fuel CMS 1.4.1 - Remote Code Execution (1)
- Date: 2021-08-16
- Origional exploit Author: 0xd0ff9
- Updated exploit Author: jtaubs1 (ice-wzl)
- Vendor Homepage: https://www.getfuelcms.com/
- Software Link: https://github.com/daylightstudio/FUEL-CMS/releases/tag/1.4.1
- Version: <= 1.4.1
- Tested on: Ubuntu - Apache2 - php5

### Update Changes
- Updated exploit to work with python3
- Exploit takes sys.argvs instead of having to pass commands in ""
- Immediatly spawns a reverse shell to a netcat listener
- Removed Burp proxy code so it functions as a stand alone RCE exploit without having to modify the code.
