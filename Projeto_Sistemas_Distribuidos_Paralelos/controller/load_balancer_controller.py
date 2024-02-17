import threading
from model.load_balancer import *
import socket
class load_balancer_controller:
    
    #como irá receber conecções de clientes e servidores temos de conseguir verificar se a conecção recebida foi um ou outro    
    def __init__ (self):
        self.load_balancer = Load_balancer()
        
        self.running_event = threading.Event()
        self.running_event.set()
        
        #começar ah procura de conecções
        self.load_balancer_thread = threading.Thread(target=self.handle_connections, args=(self.load_balancer,))
        self.load_balancer_thread.start()
        

    def handle_connections(self,load_balancer:Load_balancer):
        #ouvir conecções
        load_balancer.get_socket().listen(5)
        load_balancer.get_socket().settimeout(1)  # Defina um tempo limite para accept()

        while self.running_event.is_set():
            if len(self.load_balancer.get_servers_sockets()) > 1:
                threadsync = threading.Thread(target=self.sync_servers)
                threadsync.start()
            try:
                conection_socket, socket_address = load_balancer.get_socket().accept() #retorna um tuplo (client_socket=novo socket de conexao,client_address=(ip,port))
                if socket_address[1] == 12345: #server
                    load_balancer.add_server_address(conection_socket)
                    print(load_balancer.get_servers_sockets())
                    pass
                elif socket_address[1] == 123: #client
                    print("client")
                    self.handle_messages_thread = threading.Thread(target=self.handle_messages, args=(load_balancer, conection_socket))
                    self.handle_messages_thread.start()
            except socket.timeout as e:
                pass
        
        load_balancer.get_socket().close()
            
    #continuar
    def handle_messages(self,load_balancer:Load_balancer, connection:socket):
        connection.settimeout(0.5)
        load_balancer.get_servers_sockets()[0].settimeout(0.5)
        while self.running_event.is_set():
            try:
                data = connection.recv(1024)
                for i in range(len(self.load_balancer.get_servers_sockets())):
                    load_balancer.get_servers_sockets()[i].sendall(data)
                    response = load_balancer.get_servers_sockets()[i].recv(1024)
                    connection.sendall(response)
            except socket.timeout as e:
                pass
        connection.close()
    
    def close_conections(self):
        self.running_event.clear()        
        threads_ativas = threading.enumerate()
        for thread in reversed(threads_ativas):
            if thread.name != 'MainThread':
                thread.join()
        
    def sync_servers(self): #FUNÇAO TESTE SINCRONIZAÇAO DE DATA primeiro passa a informaçao dos clients e depois as notas 
        for socket1, socket2 in self.load_balancer.get_servers_sockets():
            try:
                socket2.sendall('get_clients')
                clients = socket2.recv(1024)
                socket1.sendall(f'handle_sync_request|{clients}')
                response = socket1.recv(1024)
                socket2.sendall(f'manage_missing_notes_request|{response}')
                response = socket2.recv(1024)
                socket1.sendall(f'add_missing_notes|{response}')


            except IndexError:
                socket2 = self.load_balancer.get_servers_sockets()[0]
                socket2.sendall('get_clients')
                clients = socket2.recv(1024)
                socket1.sendall(f'handle_sync_request|{clients}')
                response = socket1.recv(1024)
                socket2.sendall(f'manage_missing_notes_request|{response}')
                response = socket2.recv(1024)
                socket1.sendall(f'add_missing_notes|{response}')
        
        threading.Timer(20,self.sync_servers)
        