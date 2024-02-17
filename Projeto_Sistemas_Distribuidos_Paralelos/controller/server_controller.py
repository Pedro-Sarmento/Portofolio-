import ast
import json
import struct
from model.server import *
import threading
import socket

class server_controller:
    def __init__ (self):
        self.server = Server()
        self.server.load()
        self.running_event = threading.Event()
        self.running_event.set()
    
    def server_connect(self,Load_balancer_IP):   #REVER POR CAUSA DA NOVA ESTRUTURA DO CODIGO
        try:
            self.server.get_socket().connect((Load_balancer_IP, 1234)) 
            #começar ah procura de conecções
            self.server_thread = threading.Thread(target=self.handle_requests, args=(self.server,))
            self.server_thread.start() 
            return True  
        except Exception as e:
            print(e)
        
    def handle_requests(self,server:Server):
        server.get_socket().settimeout(0.5)  # Defina um tempo limite para accept()

        while self.running_event.is_set():
            try:
                data = server.get_socket().recv(1024).decode('utf-8') #retorna um tuplo (client_socket=novo socket de conexao,client_address=(ip,port))
                function_name, args = data.split('|')
                response = self.call_server_function(function_name, args)
                if isinstance(response,str):
                    server.get_socket().sendall(response.encode('utf-8'))
                elif isinstance(response,list):
                    response = pickle.dumps(response)
                    server.get_socket().sendall(response)
                elif isinstance(response,bool):
                    server.get_socket().sendall(struct.pack('B',response))
                else:
                    print("aqui nao envia nada pois o tipo Nonetype nao se envia por um socket")
            except socket.timeout as e:
                pass
        
        server.get_socket().close()

    def call_server_function(self, function_name, *args):
        function_to_call = getattr(self.server, function_name) #vai ao server buscar a funcao

        if callable(function_to_call): #verificar se é possivel chamar a funçao dentro do servidor
            #tratar dos parametros recebidos
            try:
                lista_parametros = ast.literal_eval(args[0])
            except (SyntaxError,ValueError):
                lista_parametros = args[0]
                
            #chamar respetivas funcoes
            if isinstance(lista_parametros,str):
                return function_to_call(lista_parametros)
            elif len(lista_parametros) == 2:
                return function_to_call(lista_parametros[0],lista_parametros[1])
            elif len(lista_parametros)==3:
                return function_to_call(lista_parametros[0],lista_parametros[1],lista_parametros[2])
        else:
            print("erro na funçao")
            return
    
    def close_conections(self):
        self.server.save()
        self.running_event.clear()        
        threads_ativas = threading.enumerate()
        for thread in reversed(threads_ativas):
            if thread.name != 'MainThread':
                thread.join()
    

#FALTA FAZER A REQUEST DE SYNC