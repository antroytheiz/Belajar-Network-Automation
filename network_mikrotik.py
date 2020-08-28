import paramiko

ip_address = 'ip_router'
username = 'username'
password = 'password'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# open connection to router mikrotik
ssh_client.connect(hostname=ip_address, username=username, password=password)

print("Success login to {}".format(ip_address))

# send command to router mikrotik
ssh_client.exec_command("interface bridge add name=loopback0\n")
ssh_client.exec_command("ip address add address 10.1.1.1/32 interface=loopback0\n")

# close connection from router
ssh_client.close()

