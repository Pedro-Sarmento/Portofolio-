import math

contagem_de_palavras = {} 

w_ham = 0 # nº de palavras ham
w_spam = 0 # nº de palavras spam
m_ham = 0 # nº de mails ham
m_spam = 0 # nº de mails spam

c = 0.009

def train(X):
    global w_ham, w_spam, m_ham, m_spam
    # Cálculo das frequencias absolutas
    for mail in X:
        if mail[0] == "spam":
            m_spam +=1
            for palavra in mail[1].lower().split(" "):
                if palavra.lower() not in contagem_de_palavras:
                    contagem_de_palavras[palavra] = [2, 1, 0, 0]
                else:
                    contagem_de_palavras[palavra][0] += 1
                w_spam += 1
            
        elif mail[0] == "ham":
            m_ham += 1
            for palavra in mail[1].lower().split(" "):
                if palavra.lower() not in contagem_de_palavras:
                    contagem_de_palavras[palavra] = [1, 2, 0, 0]
                else:
                    contagem_de_palavras[palavra][1] += 1
                w_ham += 1

    # Cálculo das frequencias relativas
    for palavra in contagem_de_palavras:
        contagem_de_palavras[palavra][2] = contagem_de_palavras[palavra][0] / w_spam
        contagem_de_palavras[palavra][3] = contagem_de_palavras[palavra][1] / w_ham

def classify(email, c = c):
    # Inicialização do threshold de rejeição
    threshold= -(math.log(c) + math.log(m_ham) - math.log(m_spam))

    for palavra in email.lower().split(" "):
        if palavra.lower() in contagem_de_palavras:
            threshold+= (math.log(contagem_de_palavras[palavra][0]) - math.log(contagem_de_palavras[palavra][1]))
    
    return "spam" if threshold> 0 else "ham"

def procurar_o_melhor_c():
    pass

def classify_list(lista_validacao):
    num_guesses = 0
    num_correct_guesses = 0
    num_incorrect_guesses = 0
    num_spam = 0
    num_ham = 0
    verdadeiro_positivo = 0
    verdadeiro_negativo = 0
    falso_positivo = 0
    falso_negativo = 0

    for email in lista_validacao:
        classificador = classify(email[1])
        if classificador == email[0]:
            num_correct_guesses += 1
            if classificador == 'spam':
                verdadeiro_positivo += 1
            if classificador == 'ham':
                verdadeiro_negativo += 1
        else:
            num_incorrect_guesses += 1
            if classificador == 'spam':
                falso_positivo += 1
            if classificador == 'ham':
                falso_negativo += 1

        if email[0] == 'spam':
            num_spam += 1
        if email[0] == 'ham':
            num_ham += 1
        num_guesses += 1

    print("--->Algoritmo Naive Bayes 70/15/15 <---")
    print("O algoritmo percorreu:", num_guesses, "emails!")
    print(" ")
    print("Número de emails spam avaliados:", num_spam)
    print("-> Avaliou corretamente", verdadeiro_positivo)
    print("-> Avaliou incorretamente:", num_spam - verdadeiro_positivo)
    print(" ")
    print("Número de emails ham avaliados:", num_ham)
    print("-> Avaliou corretamente", verdadeiro_negativo)
    print("-> Avaliou incorretamente:", num_ham - verdadeiro_negativo)
    print("")
    print("O algoritmo obteve uma taxa de sucesso igual a:", ((num_correct_guesses / num_guesses) * 100), "%")
    print("O algoritmo obteve uma taxa de insucesso igual a:",  (100 - (num_correct_guesses / num_guesses) * 100), "%")
    print(" ")

    print("Métricas de Classificação:")
    print("    Accuracy:", (num_correct_guesses / num_guesses))
    print("    Error rate:", (num_incorrect_guesses / num_guesses))
    print("    Sensivity:", (verdadeiro_positivo / (verdadeiro_positivo + falso_negativo)))
    print("    Specificity:", (verdadeiro_negativo / (verdadeiro_negativo + falso_positivo)))
    print("    Precision:", (verdadeiro_positivo / (verdadeiro_positivo + falso_positivo)))
    print("    Recall:", (verdadeiro_positivo / (verdadeiro_positivo + verdadeiro_negativo)))
    print(" ")
