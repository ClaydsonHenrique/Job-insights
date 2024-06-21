# Processamento de Dados CSV

## Descrição do Projeto
Este projeto tem como objetivo desenvolver relatórios detalhados sobre a quantidade de ocorrências das palavras "Python" e "Javascript" em um conjunto de dados. Além disso, inclui funcionalidades para processar e filtrar dados contidos em arquivos CSV. Para garantir a precisão e a confiabilidade das implementações, foram desenvolvidos testes automatizados rigorosos.

## Funcionalidades Implementadas

### 1. Teste de Contagem de Ocorrências (`tests/counter/test_counter.py`)
- **Objetivo:** Verificar a contagem correta das palavras "Python" e "Javascript" no arquivo `data/jobs.csv`.
- **Especificações:**
  - Contagem _case insensitive_.
  - Verificação do retorno correto da quantidade de ocorrências.

### 2. Método `read` (`src/insights/jobs.py`)
- **Objetivo:** Ler um arquivo CSV e retornar os dados no formato de uma lista de dicionários.
- **Especificações:**
  - Recebe um caminho de arquivo (`path`) como parâmetro.
  - Lê o conteúdo do arquivo CSV.
  - Armazena os dados em `self.job_list`.

### 3. Método `get_unique_job_types` (`src/insights/jobs.py`)
- **Objetivo:** Retornar uma lista de tipos de empregos únicos na coluna `job_type`.
- **Especificações:**
  - Utiliza os dados carregados previamente.
  - Ignora valores vazios.

### 4. Método `filter_by_multiple_criteria` (`src/insights/jobs.py`)
- **Objetivo:** Filtrar empregos com base em múltiplos critérios.
- **Especificações:**
  - Recebe uma lista de empregos e um dicionário `filter_criteria`.
  - Retorna empregos que correspondem a todos os critérios fornecidos.
  - Lança uma exceção `TypeError` se o filtro não for um dicionário.

### 5. Método `get_unique_industries` (`src/insights/industries.py`)
- **Objetivo:** Retornar uma lista de indústrias únicas na coluna `industry`.
- **Especificações:**
  - Utiliza os dados carregados previamente.
  - Ignora valores vazios.

### 6. Método `get_max_salary` (`src/insights/salaries.py`)
- **Objetivo:** Retornar o maior salário na coluna `max_salary`.
- **Especificações:**
  - Ignora valores ausentes.
  - Retorna o maior salário como um valor inteiro.

### 7. Método `get_min_salary` (`src/insights/salaries.py`)
- **Objetivo:** Retornar o menor salário na coluna `min_salary`.
- **Especificações:**
  - Ignora valores ausentes.
  - Retorna o menor salário como um valor inteiro.

### 8. Método `matches_salary_range` (`src/insights/salaries.py`)
- **Objetivo:** Verificar se um salário está dentro da faixa especificada.
- **Especificações:**
  - Recebe um dicionário `job` com `min_salary` e `max_salary`, e um valor `salary`.
  - Lança `ValueError` em caso de inconsistências nos dados.
  - Retorna `True` se o salário estiver na faixa, caso contrário `False`.

### 9. Filtro por Faixa Salarial (`src/insights/salaries.py`)
- **Objetivo:** Filtrar empregos com base em uma faixa salarial válida.
- **Especificações:**
  - Recebe uma lista de empregos e um valor de salário.
  - Ignora empregos com faixas salariais inválidas.
  - Retorna uma lista de empregos que correspondem ao critério salarial.

### 10. Teste de Arquivo Brasileiro (`tests/brazilian/test_brazilian_jobs.py`)
- **Objetivo:** Verificar a tradução correta das chaves de arquivos CSV em português para inglês.
- **Especificações:**
  - Chama a função `read_brazilian_file` com um caminho para um arquivo CSV em português.
  - Garante que as chaves são traduzidas corretamente para inglês.