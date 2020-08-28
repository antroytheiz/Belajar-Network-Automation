import paramiko
import time

ip_address = 'ip_router'
username = 'username'
password = 'password'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# open connection ssh to router
ssh_client.connect(hostname=ip_address, username=username, password=password)

print("Success login to {}".format(ip_address))
conn = ssh_client.invoke_shell()

# command cisco send to config cisco ios
conn.send("conf t\n")
conn.send("int lo1\n")
conn.send("ip add 10.1.1.1 255.255.255.255\n")
time.sleep(1)

output = conn.recv(65535)
print(output.decode())

# close connection ssh
ssh_client.close()

