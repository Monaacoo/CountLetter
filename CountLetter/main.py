import re
from collections import Counter

def analisar_arquivo(caminho_arquivo):
    try:
        # Abre o arquivo e lê o conteúdo
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            # Calacula o total de caracteres
            total_caracteres = len(conteudo)

            # Total de palavras e ignora pontuação e números
            palavras = re.findall(r'\b\w+\b', conteudo.lower())
            total_palavras = len(palavras)

            # Conta ocorrências de cada palavra
            ocorrencias = Counter(palavras)

            print(f'\nTotal de caracteres: {total_caracteres}')
            print(f'Total de palavras: {total_palavras}\n')

            print('Ocorrências de cada palavra (por ordem de frequência):')
            for palavra, quantidade in ocorrencias.most_common():
                print(f'{palavra}: {quantidade}')

            
            while True:
                # Permite ao usuário consultar a quantidade de ocorrências de uma palavra específica
                consulta = input('\nDigite uma palavra para ver a quantidade (ou "sair" para encerrar): ').lower()
                if consulta == 'sair':
                    break
                quantidade = ocorrencias.get(consulta, 0)
                print(f'A palavra "{consulta}" aparece {quantidade} vez(es).')

    except FileNotFoundError:
        print(f'Arquivo "{caminho_arquivo}" não encontrado.')


caminho = input('Digite o caminho do arquivo: ')
analisar_arquivo(caminho)
