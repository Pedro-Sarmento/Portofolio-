import math

def perceptron(train_data, T):
    train_data = convert_tag(train_data)
    train_data = email_to_word_counter(train_data)

    teta = create_teta(train_data)
    teta_zero = 0
    for _ in range(T):
        for email in train_data:
            if email[0] * classify(teta, email[1], teta_zero) <= 0:
                for word, count in email[1].items():
                    if word in teta:
                        teta[word] += email[0] * count
                teta_zero += email[0] 

    return teta, teta_zero

def classify(teta, email_dic, teta_zero):
    total_sum = 0
    for word, count in email_dic.items():
        if word in teta:
            total_sum += teta[word] * count
    return total_sum + teta_zero

def classify_list(lista_validacao, teta, teta_zero):
    lista_validacao = convert_tag(lista_validacao)
    lista_validacao = email_to_word_counter(lista_validacao)

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
        classificador = classify(teta, email[1], teta_zero)
        classificador = math.copysign(1, classificador)
        if math.copysign(1, classificador) == email[0]:
            num_correct_guesses += 1
            if classificador == -1:
                verdadeiro_positivo += 1
            elif classificador == 1:
                verdadeiro_negativo += 1
        else:
            num_incorrect_guesses += 1
            if classificador == -1:
                falso_positivo += 1
            elif classificador == 1:
                falso_negativo += 1
        if email[0] == -1:
            num_spam += 1
        if email[0] == 1:
            num_ham += 1
        num_guesses += 1

    print("---> Algoritmo do Perceptrão 70/15/15 <---")
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

def convert_tag(lista_emails):
    for email in lista_emails:
        if email[0] == "spam":
            email[0] = -1
        if email[0] == "ham":
            email[0] = 1
    return lista_emails

def email_to_word_counter (lista_emails):
    for email in lista_emails:
        email_word_counter = {}
        for word in email[1].split(" "):
            if word not in email_word_counter:
                email_word_counter[word] = 1
            else:
                email_word_counter[word] += 1
        email[1] = email_word_counter
    return lista_emails

def create_teta(emails_dictionary):
    teta = {}
    for email in emails_dictionary:
        for word, count in email[1].items():
            if word not in teta:
                teta[word] = 0
    return teta