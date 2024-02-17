import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from controller import client_controller
from model.client import *
    
class gui_controller:
    
    def create_center_grid (root):
        frame = tk.Frame(root, relief='flat')
        frame.config(bg='#26242f')
        frame.grid(row=0,column=0,sticky='we')
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)
        return frame

    def grid_configure(widget, urow, ucolumn):
        widget.grid(row= urow, column= ucolumn)
        widget.grid_columnconfigure(1, weight= 1)
        widget.grid_rowconfigure(1, weight=1)

    def spacer(master_frame, spacer_row, spacer_column):
        spacer = tk.Label(master_frame, text='', bg='#26242f')
        spacer.grid(row=spacer_row, column= spacer_column)
        spacer.grid_rowconfigure(1,weight=1)
        spacer.grid_columnconfigure(1,weight=1)
        return spacer

    def add_client_existing_notes(treeview, controller:client_controller): #falta fazer isto
        note_list = controller.add_client_existing_notes()
        if note_list != None:
                for note in note_list:
                    treeview.insert('', 'end', values=(note))

    def add_button_click(treeview,client_controller:client_controller):
        # Obter nota
        arquivo_selecionado = filedialog.askopenfilename(title="Selecione um arquivo",filetypes=[('Arquivos de texto','*.txt')])
        nome_arquivo = arquivo_selecionado.split('/')[-1]
        treeview.insert("", "end", values=(nome_arquivo))
        with open(arquivo_selecionado,'r')as file:
            text = file.read()
        client_controller.add_note_client(nome_arquivo,text)  

    def update_button_click(treeview:ttk.Treeview,text,controller:client_controller,add_button:tk.Button,delete_button:tk.Button,panned_client_buttons):
        if not text.get("1.0", "end-1c").strip():    
            # obter nota do server - get
            item_selecionado = treeview.selection()[0]
            if item_selecionado and treeview.item(item_selecionado, 'values'):
                note_title = treeview.item(item_selecionado, 'values')[0]
                text_note = controller.update_note_get(note_title)
                print(text_note)
                text.insert("1.0",text_note)
                treeview["selectmode"] = 'none'
                panned_client_buttons.remove(add_button)    
                panned_client_buttons.remove(delete_button)          
        else:
            item_selecionado = treeview.selection()[0]
            note_title = treeview.item(item_selecionado,'values')[0]
            text_note = text.get("1.0", tk.END)
            if controller.update_note_post(note_title, text_note):
                text.delete("1.0", tk.END)
            return True     
    
    def passer():
        pass
    
    def delete_button_click(treeview, controller):
        item_selecionado = treeview.focus()
        note_title = treeview.item(item_selecionado, 'values')[0]
        request = controller.delete_note(note_title)
        if request is True:
            treeview.delete(item_selecionado)
    

