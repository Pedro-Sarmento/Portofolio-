import socket
import threading
import os
import pickle
from model.encryption import *

# nome | nomeficheiro | texto da nota - filedata received from client
class Server():
    
    def __init__(self):
        self.clients = [] #vai guardar os dicionarios com o nome pass e lista de notas
        self.ip = None
        self.port = 12345
        self.create_socket()
        self.server_adress = (self.ip, self.port)

    def set_ip(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        return None

    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_ip()
        self.socket.bind((self.get_ip(), self.get_port())) #atribuir o seu ip e uma porta especifica de cliente
        return self.socket

    def check_if_client_exists(self,name, password):
        for client in self.clients:
            if client['name'] == name and client['password'] == password:
                return True
        return False

    def add_client(self, name, password):
        if self.check_if_client_exists(name,password) is False:
            client = {'name':name,'password':password,'notes':[]}
            self.clients.append(client)
            self.create_client_directory(name)
            return True
        else:
            return False

    def get_clients(self): 
        return self.clients
    
    def get_ip(self):
        return self.ip
    
    def get_port(self):
        return self.port

    def get_socket(self):
        return self.socket
    
    def validate_login(self, name, password): #nao esquecer da encriptaçao
        for _ in self.clients:
            if self.check_if_client_exists(name,password):
                return True
        return False
    
    #funcao que retorna os titulos de todas as notas do cliente
    def get_client_note_titles(self, client_name): # [{name:"joao",password:"fdsfds",notes:["titles1","titles2"]},                                       
        for client in self.clients:
            if client['name'] == client_name:
                return client['notes']
    
    #funcao que adiciona a nota do cliente      
    def add_client_note(self, client_name, note_title, text):
        diretorio_atual = os.getcwd()
        path_da_nota = os.path.join(diretorio_atual,'data', client_name, note_title)
        with open(path_da_nota,'w') as file:
            text = encrypt_caesar(text, 15)
            file.write(text)
        for client in self.clients:
            if client['name'] == client_name:
                    client['notes'].append(note_title)
        return None

    # UPDATE - Devolve o texto da nota pedida
    def get_client_note(self,client_name,note_title):
        diretorio_atual = os.getcwd()
        path_da_nota = os.path.join(diretorio_atual,'data', client_name, note_title)
        note = open(path_da_nota,'r',encoding='utf-8')
        conteudo = note.read()
        conteudo = decrypt_caesar(conteudo, 15)
        note.close()
        return conteudo
    
    # UPDATE - insere o texto novo na nota editada
    def update_note(self, name, title, text):
        try:
            diretorio_atual = os.getcwd()
            path_da_nota = os.path.join(diretorio_atual,'data', name, title)
            note = open(path_da_nota, 'w', encoding='utf-8')
            note.write(encrypt_caesar(text,15))
            note.close()
            return True
        except:
            return False
    
    def create_client_directory(self, name):
        diretorio_atual = os.getcwd()
        os.mkdir(os.path.join(diretorio_atual,'data', name))
        return None

    #funcao que apaga a nota que o user pediu
    def delete_client_note(self, client_name, note_title):
        diretorio_atual = os.getcwd()
        os.remove(os.path.join(diretorio_atual,'data', client_name, note_title))
        for client in self.clients:
            if client['name'] == client_name:
                client['notes'].remove(note_title)
        return True
    
    #funcoes de recuperaçao do proprio servidor
    def save(self):
        try:
            diretorio_atual = os.getcwd()
            save_file = os.path.join(diretorio_atual,'data', 'users.pkl')
            with open(save_file, 'wb') as file:
                pickle.dump(self.clients, file)
        except EOFError:
            self.clients = []
        except FileNotFoundError:
            self.clients = []
            os.makedirs(os.path.join(diretorio_atual,'data'),exist_ok=True)
            with open(save_file, 'wb') as file:
                pickle.dump(self.clients,file)

    def load(self):      #adaptei pois como o server.py esta dentro de model o diretorio q o os.getcwd ia buscar era o caminho ate ah pasta model
        try:
            diretorio_atual = os.getcwd()
            save_file = os.path.join(diretorio_atual,'data', 'users.pkl')
            with open(save_file, 'rb') as file:
                self.clients = pickle.load(file)
        except EOFError:
            self.clients = []
        except FileNotFoundError:
            self.my_list = []
            os.makedirs(os.path.join(diretorio_atual,'data'),exist_ok=True)
            with open(save_file, 'wb') as file:
                pickle.dump(self.clients,file)












    def handle_sync_request(self, external_server_client_dictionary_list):
        total_missing_data= [] #todos os dados que este servidor nao tem
        #abaixo, itera por todos os clientes no outro servidor e verifica se este os tem todos e quais notas é que faltam para poder por na matriz de notas em falta para depois passar um request para as receber, caso este server nao tenha o cliente adiciona o
        for external_server_client_index in range(len(external_server_client_dictionary_list)): 
            for this_server_client_index in range(len(self.clients)):
                #if abaixo verifica se o cliente do servidor exterior existe neste servidor, caso nao exista ele adiciona-o
                if self.check_if_client_exists(external_server_client_dictionary_list[external_server_client_index]['name'], external_server_client_dictionary_list[external_server_client_index]['password']) is False:
                    self.clients.append(external_server_client_dictionary_list[external_server_client_index])
                    self.create_client_directory(external_server_client_dictionary_list[external_server_client_index]['name'])
                    missing_notes = self.check_if_notes_exist(this_server_client_index,external_server_client_dictionary_list, external_server_client_index)
                    if len(missing_notes) == 0:
                        continue
                    else:
                        data_missing = {'client_name': external_server_client_dictionary_list[external_server_client_index]['name'],
                                        'notes': missing_notes}
                        total_missing_data.append(data_missing)
                #if abaixo vai verificar, caso o servidor atual tenha o cliente, se este tem todas as notas ou se esta alguma em falta
                elif external_server_client_dictionary_list[external_server_client_index]['name'] == self.clients[this_server_client_index]['name']:
                    missing_notes = self.check_if_notes_exist(this_server_client_index,external_server_client_dictionary_list, external_server_client_index)
                    if len(missing_notes) == 0:
                        continue
                    else:
                        data_missing = {'client_name': external_server_client_dictionary_list[external_server_client_index]['name'],
                                        'notes': missing_notes}
                        total_missing_data.append(data_missing)
        return total_missing_data

    def check_if_notes_exist(self,this_server_client_index, external_server_client_list,external_server_client_index):
        missing_notes = [] #notas que o cliente do servidor atual nao tem
        for note in external_server_client_list[external_server_client_index]['notes']: #iterar pelas notas do cliente deste servidor e do outro para verificar se um dos servers não tem notas a mais
            if note not in self.clients[this_server_client_index]['notes']:
                missing_notes.append(note)
        return missing_notes
    
    def manage_missing_notes_request(self, missing_notes_dictionary_list): #esse dicionario tem o nome do cliente e as notas que lhe faltam no outro server
        missing_notes_to_send = [] #vai ser uma matriz em que em cada lista o indice 0 é o nome do cliente e o indice 1  é um dicionario em que cada chave é o titulo da nota e o conteudo da chave o texto
        for client in missing_notes_dictionary_list:
            missing_notes = self.get_client_missing_notes(client['name'], client['notes'])
            client_missing_notes = [client['name'], missing_notes]
            missing_notes_to_send.append(client_missing_notes)
        return missing_notes_to_send

    def get_client_missing_notes(self, client_name,missing_notes_list):
        missing_notes = {}
        for note in missing_notes:
            missing_notes[note] = self.get_client_note(client_name, note) #vai adicionar ao dicionario de notas em falta uma chave que é o titulo da nota em falta e um item que é o texto da nota em falta
        return missing_notes

    def add_missing_notes(self, missing_notes_matrix):
        for name_notes in missing_notes_matrix:  #itera a matriz de notas em falta que contem em cada lista o nome do cliente no indice 0 e um dicionario que tem todas as notas 
            for title, text in name_notes[1].items(): #itera as chaves e items do dicionario ao mesmo tempo em que a chave é o titulo da nota e o item o texto
                self.add_client_note(name_notes[0],title,text)        
