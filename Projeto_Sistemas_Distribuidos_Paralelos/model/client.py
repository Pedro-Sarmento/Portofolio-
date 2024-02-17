import socket

class Client():
    def __init__(self):
        self.ip = None
        self.port = 123
        self.create_socket()
        self.name = None
        self.password = None
    
    def set_ip(self):
        self.ip = socket.gethostbyname(socket.gethostname())

    def get_ip(self):
        return self.ip
    
    def set_name(self, name: str):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def get_port(self):
        return self.port

    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_ip()
        self.socket.bind((self.get_ip(), self.get_port())) #atribuir o seu ip e uma porta especifica de cliente
        return self.socket

    def get_socket(self):
        return self.socket
    
    def set_password(self, password):
        self.password = password

    def get_password(self, password):
        return self.password
    
    