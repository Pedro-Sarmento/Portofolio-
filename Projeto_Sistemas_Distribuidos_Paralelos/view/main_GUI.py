import functools
import tkinter as tk
from tkinter import ttk
from controller.gui_controller import *
from controller.client_controller import *
from controller.load_balancer_controller import *
from controller.server_controller import *

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Note Manager")
        self.root.attributes('-alpha', 0.9)
        self.root.config(bg='#26242f')
        self.root.geometry("1080x600")
        self.root.resizable(False, False)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.home()
        self.root.mainloop()
        
    
    def home(self):
        home_frame = gui_controller.create_center_grid(self.root)
        home_label= tk.Label(home_frame, text='Home Page', bg='#26242f',fg='white',font=('courrier',25))
        gui_controller.grid_configure(home_label,1,0)
        spacer1 = gui_controller.spacer(home_frame, 2, 0) #necessita de atribuir a uma variavel ? como n ta a ser usada
        client_button = tk.Button(home_frame, text="Client", font=('Times new Roman', 20) ,height=1, width=15, command= lambda: [home_frame.destroy(), self.register_login_page()])
        gui_controller.grid_configure(client_button,3,0) 
        spacer2 = gui_controller.spacer(home_frame, 4, 0)  #necessita de atribuir a uma variavel ?     
        server_button = tk.Button(home_frame, text="Server", font=('Times new Roman', 20) ,height=1, width=15,command= lambda: [home_frame.destroy(),self.server_login_page()])
        gui_controller.grid_configure(server_button,5,0)
        spacer3 = gui_controller.spacer(home_frame, 6, 0) #necessita de atribuir a uma variavel ?
        load_balancer_button = tk.Button(home_frame, text="Load Balancer", font=('Times new Roman', 20) ,height=1, width=15,command=lambda: [home_frame.destroy, self.load_balancer_page(home_frame)])
        gui_controller.grid_configure(load_balancer_button,7,0)
    
    def register_login_page(self): #criar pagina de registo com botao registar e botao login que reencaminha para a login_page
        #cria novo cliente  
        self.client_controller = client_controller()
        
        register_login_frame = gui_controller.create_center_grid(self.root)
        buttons_frame = tk.Frame(register_login_frame,relief='flat', bg='#26242f', padx=10,pady=10)
        register_label = tk.Label(register_login_frame, text='Register', bg='#26242f', fg='white', font=('courrier',15))
        gui_controller.grid_configure(register_label,1,0)
        username_label = tk.Label(register_login_frame, text="Username: ", bg='#26242f',fg='white')
        gui_controller.grid_configure(username_label,2,0)
        name_entry = tk.Entry(register_login_frame)
        gui_controller.grid_configure(name_entry,3,0)
        passoword_label = tk.Label(register_login_frame, text="Password: ", bg='#26242f',fg='white')
        gui_controller.grid_configure(passoword_label,4,0)
        password_entry= tk.Entry(register_login_frame, textvariable="Password", show="*")
        gui_controller.grid_configure(password_entry,5,0)
        ip_label = tk.Label(register_login_frame, text="IP: ", bg='#26242f',fg='white')
        gui_controller.grid_configure(ip_label,6,0)
        ip_entry= tk.Entry(register_login_frame)
        gui_controller.grid_configure(ip_entry,7,0)  
        register_button = tk.Button(buttons_frame, width=10, text='Register',command=lambda:[self.client_page(register_login_frame) if self.client_controller.add_client(name_entry.get(),password_entry.get(), ip_entry.get()) else gui_controller.grid_configure(tk.Label(register_login_frame, text="This user exists",),8,0)])
        register_button.pack(pady=5, side='left')
        login_button= tk.Button(buttons_frame, width=10,text="LogIn", command= lambda:[self.client_page(register_login_frame) if self.client_controller.validate_login(name_entry.get(),password_entry.get(), ip_entry.get()) else gui_controller.grid_configure(tk.Label(register_login_frame, text="Wrong username or password",),8,0)] )
        login_button.pack(padx=10, pady=5, side='left')
        gui_controller.grid_configure(buttons_frame,8,0)
             
            
    def client_page(self, active_frame):
        active_frame.destroy()
        page_frame = gui_controller.create_center_grid(self.root)
        panned_client_window= tk.PanedWindow(page_frame,orient=tk.HORIZONTAL, bg='#26242f',relief='flat')
        panned_client_buttons= tk.PanedWindow(page_frame,orient=tk.HORIZONTAL, bg='#26242f',relief='flat')
        gui_controller.grid_configure(panned_client_window,0,0)
        gui_controller.grid_configure(panned_client_buttons,1,0)
        treeview_style = ttk.Style()
        treeview_style.theme_use('default')
        treeview_style.configure('Treeview', background= '#26242f', fieldbackground= '#26242f', foreground= 'white')
        treeview_style.configure('Treeview.Heading', background= '#26242f', foreground = "white")
        treeview = ttk.Treeview(panned_client_window, columns=('Notes'), show='headings')
        treeview.heading('Notes', text='Notes') 
        treeview["selectmode"] = 'browse'     
        text = tk.Text(panned_client_window)
        panned_client_window.add(treeview)
        panned_client_window.add(text)
        add_button= tk.Button(page_frame, text="Add Note", font=('Times new Roman', 15) ,height=1, width=10, command=lambda:gui_controller.add_button_click(treeview,self.client_controller))
        update_button = tk.Button(page_frame, text="Update Note", font=('Times new Roman', 15), height=1, width=10, command=lambda:[self.client_page(page_frame) if gui_controller.update_button_click(treeview,text,self.client_controller,add_button,delete_button,panned_client_buttons) else gui_controller.passer()])        
        delete_button= tk.Button(page_frame, text="Delete Note", font=('Times new Roman', 15) ,height=1, width=10, command=lambda:gui_controller.delete_button_click(treeview, self.client_controller))
        panned_client_buttons.add(add_button,pady=5)
        panned_client_buttons.add(update_button,padx=100,pady=5)
        panned_client_buttons.add(delete_button,pady=5)
        
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_client_socket) #apagar sockets se fechar janela
        gui_controller.add_client_existing_notes(treeview, self.client_controller)
        
    def fechar_client_socket(self):
        self.client_controller.close_conections()
        self.root.destroy()
        
    def load_balancer_page(self,home_frame):
        home_frame.destroy()
        self.load_balancer_controller = load_balancer_controller()
        page_frame = gui_controller.create_center_grid(self.root)
        loader_label = tk.Label(page_frame, text=f"O Load_balancer está a funcionar no ip: {self.load_balancer_controller.load_balancer.get_ip()}", bg='#26242f',fg='white',font=('courrier',15))
        gui_controller.grid_configure(loader_label,0,0)
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_load_socket) #apagar sockets se fechar janela
    
    def fechar_load_socket(self):
        self.load_balancer_controller.close_conections()
        self.root.destroy()
        
    def server_login_page(self):
        #cria novo server
        self.server_controller = server_controller()
        #self.root.protocol("WM_DELETE_WINDOW", self.fechar_server_socket) #apagar sockets se fechar janela
        server_frame = gui_controller.create_center_grid(self.root)
        server_label = tk.Label(server_frame, text="Server", bg='#26242f',fg='white',font=('courrier',15))
        gui_controller.grid_configure(server_label,1,0)
        ip_label = tk.Label(server_frame, text="Loader IP: ", bg='#26242f',fg='white')
        gui_controller.grid_configure(ip_label,2,0)
        ip_entry = tk.Entry(server_frame)
        gui_controller.grid_configure(ip_entry,3,0)
        login_button= tk.Button(server_frame, text="Connect", command= lambda:[self.server_page(server_frame) if self.server_controller.server_connect(ip_entry.get()) == True else gui_controller.grid_configure(tk.Label(server_frame, text="Wrong IP",),8,0)] )
        gui_controller.grid_configure(login_button,8,0)
        login_button.grid(pady=10)
        
    def server_page(self,server_frame):
        server_frame.destroy()
        page_frame = gui_controller.create_center_grid(self.root)
        server_label = tk.Label(page_frame, text=f"O Server está a funcionar no ip: {self.server_controller.server.get_ip()}", bg='#26242f',fg='white',font=('courrier',15))
        gui_controller.grid_configure(server_label,0,0) 
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_server_socket) #apagar sockets se fechar janela
          
    def fechar_server_socket(self):
        self.server_controller.close_conections()
        self.root.destroy()
        
        