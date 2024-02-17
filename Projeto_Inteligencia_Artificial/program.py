import NaiveBayes, perceptrao, csv_reader, ac3
import sys
import time 

sys.stdout.reconfigure(encoding="utf-8")

def opcao_escolhida():
    try:
        temp_pick = input()
    except EOFError:
        return None
    else:
        comandos = temp_pick.split(" ")
        comandos[0] = comandos[0].lower()
    return comandos
if __name__ == "__main__":
    while True:
        print("""
                 ==========================Menu==============================
                 Naive -> Executa o algoritmo de Naive Bayes(spam e ham)
                 Perceptrao -> Executa o algoritmo de perceptrão(spam e ham)
                 AC3 -> Executa o algoritmo de AC3(resolver sudoku)
                 Exit -> Encerra o programa
                 ============================================================
                 """)

        escolha = opcao_escolhida()
        lista_treino, lista_teste, lista_validacao = csv_reader.csv_reader()
        if escolha[0] == "exit" or escolha[0] == " ":
            break

        if escolha[0] == "naive":
            start_time = time.time()
            NaiveBayes.train(lista_treino)
            NaiveBayes.classify_list(lista_validacao)
            print("Tempo de execução: %s segundos." % (time.time() - start_time))

        if escolha[0] == "perceptrao":
            start_time = time.time()
            teta, teta_zero = perceptrao.perceptron(lista_treino, 10)
            perceptrao.classify_list(lista_validacao, teta, teta_zero)
            print("Tempo de execução: %s segundos." % (time.time() - start_time))

        if escolha[0] == "ac3":
            start_time = time.time()
            ac3.solve_sudoku()
            print("Tempo de execução: %s segundos." % (time.time() - start_time))