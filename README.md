
# Fuel-1.4.1-RCE-Updated
- Update to CVE-2018-16763
- Exploit Title: fuel CMS 1.4.1 - Remote Code Execution (1)
- Date: 2021-08-16
- Origional exploit Author: 0xd0ff9
- Updated exploit Author: ice-wzl
- Vendor Homepage: https://www.getfuelcms.com/
- Software Link: https://github.com/daylightstudio/FUEL-CMS/releases/tag/1.4.1
- Version: <= 1.4.1
- Tested on: Ubuntu - Apache2 - php5

### Update Changes
- Updated exploit to work with python3
- Exploit takes sys.argvs instead of having to pass commands in ""
- Immediatly spawns a reverse shell to a netcat listener
- Removed Burp proxy code so it functions as a stand alone RCE exploit without having to modify the code.
## Usage
![proof](https://user-images.githubusercontent.com/75596877/129636542-bf1b5ca2-a387-4316-b2ed-9b4030b92654.png)
- First Argument: Target ip address
- Second Argument: Attack box ip address
- Third Argument: Call back port
