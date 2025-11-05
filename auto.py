import netmiko
import paramiko
from netmiko import ConnectHandler

paramiko.Transport._preferred_kex=(
    'diffie-hellman-group1-sha1',
    'diffie-hellman-group14-sha1',
    'diffie-hellman-group-exchange-sha1'
)

# paramiko.Transport._preferred_keys=('ssh-rsa')
paramiko.Transport._preferred_pubkeys=('ssh-rsa', 'ssh-dss')
paramiko.Transport._preferred_macs=('hmac-sha1', 'hmac-sha1-06')

connection = netmiko.ConnectHandler(ip="192.168.100.1", device_type="hp_procurve")

connection.send_config_set(["vlan 20", "ip address 192.168.200.1 255.255.255.192"])
print(connection.send_command("show vlan"))
print(connection.send_command("show ip"))
connection.disconnect()