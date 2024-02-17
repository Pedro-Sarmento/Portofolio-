# [Programação Oridentada a Objetos 2021 2022](https://elearning.ual.pt/course/view.php?id=2334) - [UAL](https://autonoma.pt/) <!-- omit in toc -->

## Projeto <!-- omit in toc -->

<!-- :octocat: Repositório [Github Classroom]() -->

- [Datas Relevantes](#datas-relevantes)
- [Descrição](#descrição)
- [Instruções](#instruções)
  - [Registar utilizador (UR)](#registar-utilizador-ur)
  - [Listar utilizadores (UL)](#listar-utilizadores-ul)
  - [Registar *bookmark* (BR)](#registar-bookmark-br)
  - [Partilhar *bookmark* (BP)](#partilhar-bookmark-bp)
  - [Criar projeto (PR)](#criar-projeto-pr)
  - [Adicionar participante a projeto (PAP)](#adicionar-participante-a-projeto-pap)
  - [Consultar projeto (PC)](#consultar-projeto-pc)
  - [Adicionar *bookmark* a projeto (PAB)](#adicionar-bookmark-a-projeto-pab)
  - [Remover *bookmark* de projeto (PRB)](#remover-bookmark-de-projeto-prb)
  - [Adicionar diretório a projeto (PAD)](#adicionar-diretório-a-projeto-pad)
  - [Remover diretório de projeto (PRD)](#remover-diretório-de-projeto-prd)
  - [Criar sessão (SR)](#criar-sessão-sr)
  - [Consultar sessão (SC)](#consultar-sessão-sc)
  - [Adicionar *bookmark* a sessão (SAB)](#adicionar-bookmark-a-sessão-sab)
  - [Remover *bookmark* de sessão (SRB)](#remover-bookmark-de-sessão-srb)
  - [Gravar (G)](#gravar-g)
  - [Ler (L)](#ler-l)
- [Estrutura do projeto e repositório git](#estrutura-do-projeto-e-repositório-git)
- [Testes de *input*/*ouput*](#testes-de-inputouput)
- [Entregas](#entregas)
  - [Entrega de modelo](#entrega-de-modelo)
  - [Entrega final](#entrega-final)
- [Prova de Autoria](#prova-de-autoria)
- [Avaliação](#avaliação)

## Datas Relevantes

| Data                      | Evento                         |
| ------------------------- | ------------------------------ |
| 10/11/2021                | Disponibilização do enunciado. |
| 12/12/2021 23:59:59 GMT   | Entrega do modelo.             |
| 09/01/2022 23:59:59 GMT   | Entrega final do trabalho.     |
| 12/01/2022 --- 21/01/2022 | Provas de autoria.             |

## Descrição

Pretende-se o desenho e implementação de um sistema de gestão de marcadores web, i.e., *bookmarks*. Os *bookmarks* estão acessíveis a vários utilizadores.

Um *bookmark* simples tem um nome, um *url*, e uma data de registo. O *bookmark* pertence a um utilizador, mas pode ser partilhado com um conjunto de utilizadores. O nome do *bookmark* é único no conjunto de *bookmarks* do utilizador.

Existem *projetos*, que correspondem a coleções de *bookmarks*. Para associar um *bookmark* a um projeto, o utilizador deve ser o autor do *bookmark*, ou ter acesso através de uma partilha.

Um projeto tem um nome e uma data de criação. Além de *bookmarks*, um projeto pode conter diretórios de *bookmarks*. Um diretório pode também conter outros diretórios.

Além do utilizador criador do projeto, podem ainda ser associados mais dois tipos de utilizador participante: gestores e membros. Um gestor de um projeto pode adicionar e remover *bookmarks* e diretórios; um membro de um projeto pode adicionar e remover *bookmarks*. O criador do projeto é também considerado gestor.

Existem ainda *sessões*, que correspondem a coleções de *bookmarks*, sem diretórios. Uma sessão tem um nome único, uma data de criação, e pertence a um utilizador.

Os *bookmark* podem ser assinalados como *pessoal*, *trabalho*, ou *outros*, pelos utilizadores aos quais pertencem (ver [Tabela 1](#tab-types)).

<div id="tab-types">Tabela 1: Tipos de <i>bookmark</i>, com indicação de ordem e restrições de partilha respetivas.</div>

| Ordem | Tipo de *bookmark* | Restrição de partilha                                                                 |
| ----- | ------------------ | ------------------------------------------------------------------------------------- |
| 1     | Pessoal            | Não permite partilha, e pode ser utilizado numa sessão.                               |
| 2     | Trabalho           | Permite partilha direta com utilizadores, e pode ser utilizado num projeto ou sessão. |
| 3     | Outro              | Permite partilha direta com utilizadores, e pode ser utilizado num projeto.           |

## Instruções

Na descrição das várias instruções é indicada a sua sintaxe. Os argumentos são separados por espaços em branco, e cada linha é terminada por um caráter fim de linha.

Para cada instrução é indicada a lista de expressões de saída, quer para execuções com sucesso, quer para insucesso.

No caso de insucesso só deve surgir uma mensagem de erro. Verificando-se várias situações de insucesso em simultâneo, deve surgir apenas a mensagem do primeiro cenário, de acordo com a ordem de saídas de insucesso descritas para cada instrução.

Caso o utilizador introduza uma instrução inválida, ou seja, não prevista na lista de instruções desta secção, ou um número de parâmetros errado para uma instrução existente, o programa deve escrever:

    Instrução inválida.

Pode assumir que não existem erros de representação de informação (e.g., texto em vez de valores numéricos).

Cada instrução será utilizada corretamente nos testes de utilização, i.e., se o número de parâmetros for correto, pode assumir que não existem erros de representação de informação (e.g., texto em vez de valores numéricos).

A descrição de cada instrução pretende ser exaustiva, e sem ambiguidades. Não deve ser possível optar entre vários comportamentos possíveis na mesma situação. Se essa situação ocorrer deve entrar em contacto com equipa docente.

A implementação não deve suportar mais instruções do que as que estão descritas.

O formato de dados utilizado é o `AAAAMMDD`, ou seja, utiliza oito números indicando ano (`AAAA`), mês (`MM`), e dia (`DD`).

O programa termina quando for introduzida uma linha em branco, fora do contexto de uma instrução.

### Registar utilizador (UR)

Regista um novo utilizador.

`Nome` é o nome do utilizador a registar, e pode conter espaços. `IdentificadorUtilizador` é o identificador do utilizador, único no conjunto de utilizadores, gerado automaticamente numa sequência de números inteiros iniciada em 1.

Entrada:

    UR Nome

Saída com sucesso:

    Utilizador registado com identificador IdentificadorUtilizador.

### Listar utilizadores (UL)

Lista todos os utilizadores registados, por ordem crescentes de identificador de utilizador.

`IdentificadorUtilizador` é o identificador de um utilizador. `NomeUtilizador` é o nome de um utilizador.

Entrada:

      UL

Saída com sucesso:

      IdentificadorUtilizador NomeUtilizador
      IdentificadorUtilizador NomeUtilizador
      ...

Saída com insucesso:

- Quando não existem utilizadores registados.

      Sem utilizadores registados.

### Registar *bookmark* (BR)

Regista um novo *bookmark* para um utilizador.

`IdentificadorUtilizador` é o identificador único de um utilizador. `Data` é uma data no formato `AAAAMMDD`. `TipoBookmark` é o tipo do bookmark, de acordo com a [Tabela 1](#tab-types). `NomeBookmark` é o nome de um *bookmark*, pode conter espaços, e é único no conjunto de *bookmarks* do utilizador. `URL` é o *url* do *bookmark*.

Entrada:

      BR IdentificadorUtilizador Data TipoBookmark
      NomeBookmark
      URL

Saída com sucesso:

      Bookmark registado com sucesso.

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o nome do *bookmark* já foi utilizado pelo utilizador para registar outro *bookmark*.
  
      Bookmark existente.

- Quando a data é inválida.
  
      Data inválida.

- Quando o tipo é inválido.
  
      Tipo inválido.

### Partilhar *bookmark* (BP)

Efetuar a partilha de um *bookmark* com outro utilizador.

`IdentificadorUtilizador` é o identificador de um utilizador que registou o *bookmark*. `IdentificadorUtilizadorPartilha` é o identificador do utilizador com o qual o *bookmark* será partilhado. `NomeBookmark` é o nome de um *bookmark*, pode conter espaços, e é único no conjunto de *bookmarks* do utilizador que o registou.

Entrada:

      BP IdentificadorUtilizador IdentificadorUtilizadorPartilha
      NomeBookmark

Saída com sucesso:

      Bookmark partilhado com sucesso.

Saída com insucesso:

- Quando pelo menos um dos identificadores de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o nome do *bookmark* não corresponde a um *bookmark* registado pelo utilizador.
  
      Bookmark inexistente.

- Quando o *bookmark* não tem permissões para ser partilhado (ver [Tabela 1](#tab-types)).

      Sem permissões.

### Criar projeto (PR)

Cria um novo projeto, propriedade de um utilizador.

`IdentificadorUtilizador` é o identificador único de um utilizador, criador do projeto. `Data` é uma data no formato `AAAAMMDD`. `NomeProjeto` é o nome de um projeto, que pode conter espaços. `IdentificadorProjeto` é o identificador do projeto, único no conjunto de projetos do utilizador, gerado automaticamente (para cada utilizador), numa sequência de números inteiros iniciada em 1.

Entrada:

      PR IdentificadorUtilizador Data
      NomeProjeto

Saída com sucesso:

      Projeto registado com o identificador IdentificadorProjeto.

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando a data é inválida.
  
      Data inválida.

### Adicionar participante a projeto (PAP)

Adiciona um novo participante a um projeto de um utilizador.

`IdentificadorUtilizador` é o identificador único de um utilizador, criador do projeto. `IdentificadorProjeto` é o identificador do projeto. `IdentificadorUtilizadorParticipante` é o identificador único de um utilizador a adicionar como participante no projeto. `TipoDeParticipante` é o tipo de participante, i.e., `Gestor` ou `Membro`.

Entrada:

      PAP IdentificadorUtilizador IdentificadorProjeto IdentificadorUtilizadorParticipante TipoDeParticipante

Saída com sucesso:

      Utilizador adicionado a projeto com sucesso.

Saída com insucesso:

- Quando um dos identificadores de utilizador indicados não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando não existe um projeto com o identificador indicado associado ao utilizador.

      Projeto inexistente.

### Consultar projeto (PC)

Mostra o conjunto de *bookmark* num projeto, incluindo os diretórios e sub-diretórios (se existirem).

Os *bookmarks* são mostrados por ordem de data de registo, e por ordem lexicográfico de nome dentro da mesma data. Os diretórios são mostrados por ordem lexicográfica de nome, em cada nível da hierarquia de diretórios.

`IdentificadorUtilizador` é o identificador do utilizador criador do projeto, e `IdentificadorProjeto` é o identificador do projeto. `NomeProjeto` é o nome do projeto. `NomeBookmark` é o nome de um *bookmark*, e `URL` é o url do *bookmark*. `NomeDiretório` é o nome de um diretório ou sub-diretório do projeto. `IdentificadorUtilizadorCriadorDeBookmark` é o identificador do utilizador que registou inicialmente o *bookmark*. `IdentificadorUtilizadorQueAdicionou` é o identificador do utilizador participante no projeto que adicionou o *bookmark*.

Entrada:

      PC IdentificadorUtilizador IdentificadorProjeto

Saída com sucesso:

      NomeProjeto
      NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      ...
      NomeDiretório : NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      NomeDiretório : NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      ...
      NomeDiretório > NomeDiretório : NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      NomeDiretório > NomeDiretório : NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      ...
      NomeDiretório > NomeDiretório > NomeDiretório : NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      NomeDiretório > NomeDiretório > NomeDiretório : NomeBookmark IdentificadorUtilizadorCriadorDeBookmark IdentificadorUtilizadorQueAdicionou [URL]
      ...

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o identificador de projeto não corresponde a um projeto registado.

      Projeto inexistente.

### Adicionar *bookmark* a projeto (PAB)

Adiciona um *bookmark* a um projeto de um utilizador.

`IdentificadorUtilizador` é o identificador do utilizador criador do projeto, e `IdentificadorProjeto` é o identificador do projeto. `IdentificadorUtilizadorParticipante` é o identificador de um utilizador participante no projeto, que pretende adicionar o *bookmark*. `IdentificadorUtilizadorBookmark` é o identificador do utilizador que registou o bookmark. `NomeBookmark` é o nome do *bookmark*, único no conjunto de *bookmarks* do utilizador que o registou. `NomeDiretório` é o nome de um diretório ou sub-diretório do projeto.

Os identificadores de utilizador `IdentificadorUtilizadorParticipante` e `IdentificadorUtilizadorBookmark` podem ser diferentes, caso o *bookmark* tenha sido partilhado.

Entrada:

      PAB IdentificadorUtilizador IdentificadorProjeto IdentificadorUtilizadorParticipante
      IdentificadorUtilizadorBookmark NomeBookmark
      NomeDiretório > NomeDiretório > ...

Saída com sucesso:

      Bookmark associado a projeto com sucesso.

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o identificador de projeto não corresponde a um projeto registado.

      Projeto inexistente.

- Quando o nome do *bookmark* não corresponde a um *bookmark* registado pelo utilizador, ou partilhado com o utilizador.

      Bookmark inexistente.

- Quando o tipo do *bookmark* não permite a operação.

      Sem permissões.

### Remover *bookmark* de projeto (PRB)

Remove um *bookmark* de um projeto.

`IdentificadorUtilizador` é o identificador do utilizador criador do projeto, e `IdentificadorProjeto` é o identificador do projeto. `IdentificadorUtilizadorParticipante` é o identificador de um utilizador participante no projeto. `IdentificadorUtilizadorBookmark` é o identificador do utilizador que registou o bookmark. `NomeBookmark` é o nome do *bookmark*, único no conjunto de *bookmarks* do utilizador que o registou.

Os identificadores de utilizador `IdentificadorUtilizadorParticipante` e `IdentificadorUtilizadorBookmark` podem ser diferentes, caso o *bookmark* tenha sido partilhado.


Entrada:

      PAB IdentificadorUtilizador IdentificadorProjeto IdentificadorUtilizadorParticipante
      IdentificadorUtilizadorBookmark NomeBookmark

Saída com sucesso:

      Bookmark removido de projeto com sucesso.

Saída com insucesso:

- Quando pelo menos um dos identificadores de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o identificador de projeto não corresponde a um projeto registado.

      Projeto inexistente.

- Quando o nome do *bookmark* não está associado ao projeto.

      Bookmark inexistente no projeto.

### Adicionar diretório a projeto (PAD)

Regista um novo diretório no projeto. O diretório pode ser criado na raiz do projeto, ou numa hierarquia de diretórios existentes.

`IdentificadorUtilizador` é o identificador do utilizador criador do projeto, e `IdentificadorProjeto` é o identificador do projeto. `IdentificadorUtilizadorParticipante` é o identificador de um utilizador participante no projeto, que adiciona o diretório. `NomeDiretório` é o nome de um diretório. Uma hierarquia de diretórios é representada recorrendo ao símbolo `>`.

Entrada:

      PAB IdentificadorUtilizador IdentificadorProjeto IdentificadorUtilizadorParticipante
      NomeDiretório > NomeDiretório > ...

Saída com sucesso:

      Diretório criado com sucesso.

Saída com insucesso:

- Quando pelo menos um dos identificadores de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o identificador de projeto não corresponde a um projeto registado.

      Projeto inexistente.

- Quando o utilizador participante não tem permissões para a operação.

      Sem permissões.

- Quando o nome do diretório já existe no projeto.

      Diretório existente no projeto.

- Quando a hierarquia de diretórios indicada não existe no projeto.

      Hierarquia de diretórios inválida.

### Remover diretório de projeto (PRD)

Remove um diretório, ou hierarquia de diretórios, de um projeto.

`IdentificadorUtilizador` é o identificador do utilizador criador do projeto, e `IdentificadorProjeto` é o identificador do projeto. `IdentificadorUtilizadorParticipante` é o identificador de um utilizador participante no projeto, que remove o diretório. `NomeDiretório` é o nome de um diretório. Uma hierarquia de diretórios é representada recorrendo ao símbolo `>`.

Entrada:

      PRD IdentificadorUtilizador IdentificadorProjeto IdentificadorUtilizadorParticipante
      NomeDiretório > NomeDiretório > ...

Saída com sucesso:

      Diretório removido com sucesso.

Saída com insucesso:

- Quando pelo menos um dos identificadores de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando o identificador de projeto não corresponde a um projeto registado.

      Projeto inexistente.

- Quando o utilizador participante não tem permissões para a operação.

      Sem permissões.

- Quando a hierarquia de diretórios indicada não existe no projeto.

      Hierarquia de diretórios inválida.

### Criar sessão (SR)

Cria uma nova sessão para um utilizador.

`IdentificadorUtilizador` é o identificador de um utilizador. `Data` é uma data no formato `AAAAMMDD`. `NomeSessão` é o nome da sessão, único no conjunto de sessões do utilizador.

Entrada:

      SR IdentificadorUtilizador Data
      NomeSessão

Saída com sucesso:

      Sessão criada com sucesso.

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando a data é inválida.
  
      Data inválida.

- Quando já existe uma sessão com o nome indicado.
  
      Sessão existente.

### Consultar sessão (SC)

Mostra os *bookmarks* numa sessão, ordenados de acordo com a coluna de Ordem da [Tabela 1](#tab-types). Dentro do mesmo tipo, são ordenados lexicograficamente por nome. Dentro do mesmo nome, são ordenados por ordem de identificador de utilizador que registou o *bookmark*.

`IdentificadorUtilizador` é o identificador do utilizador criador da sessão. `NomeSessão` é o nome da sessão, único no conjunto de sessões do utilizador. `NomeBookmark` e `URL` são o nome e endereço de um bookmark.

Entrada:

      SC IdentificadorUtilizador
      NomeSessão

Saída com sucesso:

      Data
      NomeBookmark [URL]
      NomeBookmark [URL]
      ...

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando não existe uma sessão com o nome indicado associada ao utilizador.

      Sessão inexistente.

### Adicionar *bookmark* a sessão (SAB)

Adiciona um *bookmark* a uma sessão de um utilizador.

`IdentificadorUtilizador` é o identificador do utilizador criador da sessão. `NomeSessão` é o nome da sessão, único no conjunto de sessões do utilizador. `IdentificadorUtilizadorBookmark` é o identificador do utilizador que registou o bookmark. `NomeBookmark` é o nome do *bookmark*, único no conjunto de *bookmarks* do utilizador que o registou.

Os identificadores de utilizador `IdentificadorUtilizador` e `IdentificadorUtilizadorBookmark` podem ser diferentes, caso o *bookmark* tenha sido partilhado.

Entrada:

      SAB IdentificadorUtilizador
      NomeSessão
      IdentificadorUtilizadorBookmark NomeBookmark

Saída com sucesso:

      Bookmark associado a sessão com sucesso.

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando não existe uma sessão com o nome indicado associada ao utilizador.

      Sessão inexistente.

- Quando o nome do *bookmark* não corresponde a um *bookmark* registado pelo utilizador, ou partilhado com o utilizador.

      Bookmark inexistente.

- Quando o tipo do *bookmark* não permite a operação.

      Sem permissões.

### Remover *bookmark* de sessão (SRB)

Remove um *bookmark* de uma sessão.

`IdentificadorUtilizador` é o identificador do utilizador criador da sessão. `NomeSessão` é o nome da sessão, único no conjunto de sessões do utilizador. `IdentificadorUtilizadorBookmark` é o identificador do utilizador que registou o bookmark. `NomeBookmark` é o nome do *bookmark*, único no conjunto de *bookmarks* do utilizador que o registou.

Os identificadores de utilizador `IdentificadorUtilizador` e `IdentificadorUtilizadorBookmark` podem ser diferentes, caso o *bookmark* tenha sido partilhado.

Entrada:

      SRB IdentificadorUtilizador
      NomeSessão
      IdentificadorUtilizadorBookmark NomeBookmark

Saída com sucesso:

      Bookmark removido de sessão com sucesso.

Saída com insucesso:

- Quando o identificador de utilizador não corresponde a um identificador registado.

      Utilizador inexistente.

- Quando não existe uma sessão com o nome indicado associada ao utilizador.

      Sessão inexistente.

- Quando o *bookmark* não corresponde a um *bookmark* associado à sessão.

      Bookmark inexistente na sessão.

### Gravar (G)

Grava o estado atual completo do programa num ficheiro.

`NomeFicheiro` é o caminho completo, ou relativo, de um ficheiro a ser criado (se não existir) ou re-escrito.

Entrada:

      G NomeFicheiro

Saída com sucesso:

      Ficheiro gravado com sucesso.

### Ler (L)

Lê o estado do programa de um ficheiro.

`NomeFicheiro` é o caminho completo, ou relativo, de um ficheiro a ser criado ou re-escrito.

Entrada:

      L NomeFicheiro

Saída com sucesso:

      Ficheiro lido com sucesso.

Saída com insucesso:

- Quando o ficheiro não existe

      Ficheiro inexistente.

## Estrutura do projeto e repositório git

O desenvolvimento do projeto deve ser suportado pelo repositório no Github Classroom.

O código deve ser mantido dentro de um diretório `src`.

O repositório *template* de referência está disponível em <https://github.com/UAL-POO/POO-2021-2022-projeto>

Para efetuar as atualizações:

1. Registar o repositório como `upstream` (só deve acontecer uma vez)

        git remote add upstream http://github.com/UAL-POO/POO-2021-2022-projeto

2. Atualizar o `upstream` (sempre que existirem atualizações)

        git fetch upstream

3. Obter as alterações (e.g., ficheiro `README.md`)

        git checkout upstream/main README.md

## Testes de *input*/*ouput*

O projeto é validado através de um conjunto de baterias de teste de *input*/*ouput*.

Cada bateria é constituída por um ficheiro de entrada e outro e saída. O ficheiro de entrada contém uma sequência de instruções a passar pelo programa que, por sua vez, deve produzir uma sequência de saída exatamente igual ao ficheiro de saída. A comparação será feita *byte* a *byte*, pelo que não podem existir quaisquer diferenças para o programa ser considerado válido.

Os grupos de trabalho devem utilizar as baterias públicas para validar o desenvolvimento do projeto.

As baterias serão distribuídas através do repositório git de referência, na diretoria `iotests` (será necessário registar o repositório de referência como `upstream`, de acordo com as instruções na secção anterior.).

## Entregas

### Entrega de modelo

O modelo deve ser entregue no Moodle, através de um ficheiro `.pdf` ou `.svg`, onde deve constar o diagrama de classes detalhado da solução proposta (em formato vetorial).

### Entrega final

A entrega do projeto é feita no *GitHub Classroom* e na plataforma de *e-learning*.

A entrega no *e-learning* corresponde a um ficheiro `zip` do repositório *GitHub Classroom*.

Deve existir, na raiz do repositório:

- Um diretório `src`, que deverá conter todo o código fonte, organizado por *packages*;
- Um ficheiro chamado `Program.java`, com uma classe pública chamada `Program`, na raiz do diretório `src`. A classe será executada com as instruções dos testes;
- Um ficheiro de relatório `REPORT.pdf` com a identificação dos elementos do grupo de trabalho, diagramas, e eventuais comentários relativos a estratégias de implementação adotadas, e/ou à distribuição de tarefas.

O código fonte entregue será sujeito a validação com um conjunto de testes reservado para esse efeito.

A ausência de identificação individual no ficheiro de relatório implica a anulação da participação individual no projeto.

## Prova de Autoria

Todos os projetos entregues serão sujeitos a prova de autoria. Para esse efeito, cada grupo terá que efetuar uma discussão com a docência, de forma a demonstrar que o código entregue foi de facto feito pelo grupo, e que a distribuição de trabalho foi equilibrada.

O resultado da prova determina uma ponderação individual a aplicar à nota final do projeto.

O calendário das provas de autoria será disponibilizado no *e-learning*, após o prazo de entrega da implementação do projeto.

A não comparência na prova de autoria implica a anulação da participação individual no projeto.

## Avaliação

O projeto corresponde a 50% (10% + 40%) da avaliação contínua, e tem duas componentes:

- 20% Modelo de solução (primeira entrega);
  - Representa 10% da nota final de avaliação contínua (2 valores);
  - Consiste num diagrama de classes detalhado.
- 80% Implementação (entrega final).
  - Representa 40% da nota final de avaliação contínua (8 valores);
  - Está sujeita a prova de autoria, i.e., a nota individual da implementação do projeto é resultado da ponderação da prova de autoria e nota da implementação;
  - A implementação estrita de todas as instruções descritas neste enunciado assegura, sem prejuízo de reprovação por irregularidade académica, a nota mínima de 10 na implementação (antes da ponderação individual);
  - Pode ser utilizada para substituir a parte prática do exame.

A implementação do projeto é avaliada com base em duas componentes: quantitativa (*A*), e qualitativa (*B*). A nota final da implementação é determinada por *(0.5 x A) + (0.5 x B)*.

| Instrução | Peso      |
| --------- | --------- |
| UR        | 1 valor   |
| UL        | 1 valor   |
| BR        | 1 valor   |
| BP        | 1 valor   |
| PR        | 1 valor   |
| PAP       | 1 valor   |
| PC        | 1 valor   |
| PAB       | 2 valor   |
| PRB       | 2 valor   |
| PAD       | 2 valor   |
| PRD       | 2 valor   |
| SR        | 1 valor   |
| SC        | 1 valor   |
| SAB       | 1 valor   |
| SRB       | 1 valor   |
| G         | 0.5 valor |
| L         | 0.5 valor |

A avaliação qualitativa irá considerar que existem várias formas de resolver o problema descrito, mas que se exige a utilização dos instrumentos e métodos apresentados na unidade curricular de Programação Orientada a Objetos, nomeadamente:

- Orientação a objetos;
- Definição de tipos de dados com recurso a interfaces e classes abstratas, quando apropriado;
- Justificação clara para os atributos e operações dos objetos;
- Organização da solução coerente com a metodologia apresentada na unidade curricular.

A utilização de pacotes não incluídos na distribuição padrão Java (JDK 17) está sujeita a aprovação pela docência.

As notas finais do projeto, incluindo modelo e notas individuais de implementação, serão disponibilizadas no *e-learning*.
