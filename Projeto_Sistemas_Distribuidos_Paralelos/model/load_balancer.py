import socket

class Load_balancer():
    def __init__(self):
        self.servers_sockets = []
        self.ip = None
        self.port = 1234
        self.create_socket()        

    #region getters/setters 
    
    def add_server_address(self, server_socket):
        self.servers_sockets.append(server_socket)
    
    def get_servers_sockets(self):
        return self.servers_sockets
    
    def set_ip(self):
        self.ip = socket.gethostbyname(socket.gethostname())

    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_ip()
        self.socket.bind((self.get_ip(), self.get_port())) #atribuir o seu ip e uma porta especifica de cliente

    def get_port(self):
        return self.port

    def get_socket(self):
        return self.socket
    
    def get_ip(self):
        return self.ip
    #endregion

    
    
    