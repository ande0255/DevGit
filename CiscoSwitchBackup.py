from getpass import getpass

from netmiko import ConnectHandler

password = getpass()

ipaddrs = ["192.168.160.201", "10.10.10.11"]

# A list comprehension
devices = [
    {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "loopedback",
        "password": password,
    }
    for ip in ipaddrs
]

for device in devices:
    print(f'Connecting to the device: {device["host"]}')

    with ConnectHandler(**device) as net_connect:  # Using Context Manager
        output = net_connect.send_command('sh ver')
        output = net_connect.send_command('sh run')
     # Inside the connection

        # Notice here I didn't call the `net_connect.disconnect()`
        # because the `with` statement automatically disconnects the session.

    # On this indentation level (4 spaces), the connection is terminated
    print(output)