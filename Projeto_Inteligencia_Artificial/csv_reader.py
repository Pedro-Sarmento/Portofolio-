import csv
from random import shuffle

blacklist = ["!", "?", ",", "-", ".", "/", ";", "_", "{", "}", "%", ":", "(", ")", "<", ">"]  # usado para filtrar os caracteres que não sao palavras

def csv_reader():
    treino = []
    teste = []
    validacao = []
    with open("spam.csv", "r") as ficheiro:
        reader = csv.reader(ficheiro)
        emails_todos = []
        for email in reader:
            for word in email[1].lower().split(" "):
                word = word.lower()
                for char in blacklist:
                    word.replace(char, "")
            emails_todos.append(email)
        emails_todos.remove(emails_todos[0])
        shuffle(emails_todos)
        for i in range(len(emails_todos)):
            if i < round(len(emails_todos) * 0.7):
                treino.append(emails_todos[i])
            elif i < round(len(emails_todos) * 0.7 + len(emails_todos) * 0.15):
                teste.append(emails_todos[i])
            else:
                validacao.append(emails_todos[i])
        return treino, teste, validacao