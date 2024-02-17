import pickle
import struct
from model.client import *
from model.load_balancer import *
from model.load_balancer import *
import os

class client_controller:
    def __init__ (self):
        self.client = Client()
        
    def create_client(self,name, password):
        self.client.set_name(name)
        self.client.set_password(password)

    def client_connect(self,Load_balancer_IP): 
        try:
            self.client.get_socket().connect((Load_balancer_IP, 1234))  
        except Exception as e:
            print(e)
            return "Server Down or Not Found"

    def add_client(self,name, password,ip):
        self.client_connect(ip) #correto
        args = [name, password]
        message = f"add_client|{args}"
        server_response = self.send_request(message)
        if server_response == True:
            self.create_client(name,password)
            return True
        else:
            return False
        
    def validate_login(self,name, password,ip):
        #fazer conexao com o server para verificar a existencia do cliente se nao existir cria um novo
        self.client_connect(ip) #correto
        args = [name, password]
        message = f"validate_login|{args}"
        server_response = self.send_request(message)
        if server_response == True:
            self.create_client(name,password)
            return True
        else:
            return False

    def send_request(self, message):
        try:
            client_socket = self.client.get_socket()
            client_socket.settimeout(1)              
            client_socket.sendall(message.encode())          
            response = client_socket.recv(1024) #None , bool em struct , lista em pickle e string encode
            if response is None:
                return response
            else: 
                try:
                    dados_desserializados:list = pickle.loads(response)
                    return dados_desserializados
                except pickle.UnpicklingError:
                    try:
                        response = struct.unpack('?',response)[0]
                        return response
                    except struct.error as e:
                        response = response.decode('utf-8')
                        return response   
        except socket.timeout as e:
            pass

    #funcao que da add ah nota no cliente
    def add_note_client(self,title:str,text:str):
        message = f"add_client_note|{[self.client.get_name(),title,text]}"
        server_response = self.send_request(message)
        return server_response
    
    #funcao que irá buscar a respetiva nota que o cliente pediu
    def update_note_get(self,note_title):
        args = [self.client.get_name(), note_title]
        message = f"get_client_note|{args}"
        server_response = self.send_request(message)
        return server_response
    
    #funcao que irá dar update na base de dados ah nota do cliente
    def update_note_post(self,note_title, text): #falta so fazer um para reotnar a nota e outro para dar save no texto
        args = [self.client.get_name(), note_title, text]
        message = f"update_note|{args}"
        server_response = self.send_request(message)
        return server_response
    
    #funcao que apaga a nota respetiva do cliente
    def delete_note(self, note_title):
        args = [self.client.get_name(),note_title]
        message = f'delete_client_note|{args}'
        server_response = self.send_request(message)
        if server_response == True: 
            return True

    #função de abertura para ir buscar todos os titulos das notas do cliente
    def add_client_existing_notes(self):
        name = self.client.get_name()
        message = f'get_client_note_titles|{name}'
        server_response = self.send_request(message)
        return server_response

    def send_msg(self):
        message = "oha"
        self.client.get_socket().sendall(message.encode())

    def add_note_post(self,title):
        args = [self.client.get_name(), title]
        message = f'add_client_note|{args}'
        server_response = self.send_request(message)
        
    def close_conections(self):
        self.client.get_socket().close()

