import yaml
from .server import Server

def load_config(path):
    with open(path) as configuration_file:
        configuration = yaml.load(configuration_file,Loader=yaml.FullLoader)
    return configuration


def server_from_config(config):
    server_dict = {}
    for entry in config.get('hosts',[]):
        server_dict[entry['host']]= [Server(server_name) for server_name in entry['servers']]
    return server_dict


def healthcheck(register):
    for host in register:
        for server in register[host]:
            server.checkHealth()
    return register


def get_healthy_server(host,server_dict):
    if(server_dict[host][0]):
        return server_dict[host][0]
    else:
        return False

