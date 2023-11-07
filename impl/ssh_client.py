import paramiko

class SSHClient():

    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def ssh_connect(self, host, user, password):
        self.client.connect(hostname=host, port=22, username=user, password=password)

    def ssh_disconnect(self):
        self.client.close()

    def ssh_execute(self, cmd=""):
        return self.client.exec_command(cmd)    
            


