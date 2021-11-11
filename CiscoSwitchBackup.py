# --- This script has been tested on Python3 v.3.6.9 running on Ubuntu 16.04 and 20.04 LTS ---
#
#  This script is meant to be a lightweight solution for backing up Cisco Switch configs, utilizing GetPass to avoid the need for encryption of SSH Admin creds or statically
#  configuring them in script, values can be manipulated as needed
#
# --- Below is quick overview of how to configure Python Virtual Environment to install packages and run script from Linux jumpbox
#
# --- Create and move into Python Virtual Environment :
#
# python3 -m venv (dirname)
# source (dirname)/bin/activate
#
# --- Verify Python 3 is installed, if not install:
#
# python --version
# sudo apt install python3
#
# --- Verify PIP is installed, if not install:
#
# python3 -m pip --version
# python3 pip install
#
# --- Create requirements.txt file in Venv to install packages by issuing the below command :
#
# nano requests.txt
#
#--- This will create empty requirements.txt file and drop you inter text editor, copy / paste the below packages (remove any # or spaces) :
#
# napalm>=2.4.0
# ncclient>=0.6.3
# netmiko>=2.3.3
# pyang>=1.7.5
# PyYAML>=5.1
# requests>=2.21.0
# urllib3>=1.24.1
# xmltodict>=0.12.0
# wheel
#
# --- Use key combo below to exit text editor while saving changes:
#
# ctrl x + y + enter (Select Y to confirm saving changes to file
#
# --- Install Python "requests" library from PIP:
#
# pip install requests
#
#--- Issue below command to save the current state of Py Venv: 
#
#pip freeze
#
#--- Install GetPass for use within Python script:
#
# sudo apt install getpass
#
# Below is the Python script for retrieving "sh ver" and "sh run" from Cisco switches, comments added to explain logic / values required for script to work properly
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

ipaddrs = ["192.168.160.201", "10.10.10.11"] # List all IP Addresses for script to run against

devices = [
    {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "UserName",
        "password": password,
    }
    for ip in ipaddrs
]

for device in devices:
    print(f'Connecting to the device: {device["host"]}')

    with ConnectHandler(**device) as net_connect:  # Using Context Manager
        output = net_connect.send_command('sh ver')
        output = net_connect.send_command('sh run')

        # Notice here I didn't call the `net_connect.disconnect()`
        # because the `with` statement automatically disconnects the session.

    # On this indentation level (4 spaces), the connection is terminated
    print(output)
