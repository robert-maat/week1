import os
from netmiko import ConnectHandler
from getpass import getpass

homedir = os.path.expanduser('~')
filename = ".cred" 
credfile = homedir + "/" + filename

with open(credfile) as f:
    cred = f.read()

username, password = cred.split(":")
username = username.strip()
password = password.strip()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": username, 
    "password": password, 
    "port": "22",
}

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": username, 
    "password": password, 
    "port": "22",
}

conDev = ConnectHandler(**nxos1)
print(conDev.find_prompt())


conDev = ConnectHandler(**nxos2)
print(conDev.find_prompt())


