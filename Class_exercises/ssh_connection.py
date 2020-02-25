from paramiko import SSHClient

def connect_to_server(srv):
    ssh=SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(srv)
    srv_in, srv_out, srv_err = ssh.exec_command('ls')
    return srv_out


var = connect_to_server('vaiolabs.io')

print(var)