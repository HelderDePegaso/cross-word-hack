
###
###
###
###
###
###
###
###

import os
import argparse
import pandas as pd



listOfWords = []


df: pd.DataFrame = None



# Variables for the cli processing   

# Variable for the new project
source = ""
new_project = ""
language = "None"
database = ""


# Variable for the add data
add_data = ""
project_path = ""

final_dir = ""

def loadDF(caminho: str):
    
    
    #if os.path.exists(caminho):
    #    return pd.read_excel(caminho, engine="openpyxl")  # Ler o arquivo existente
    #else:
    
    return pd.DataFrame(listOfWords, columns=["N", "Word", "freq_num", "freq_per", "total_analizide", "font_analizided"])  # Criar um DataFrame vazio
    
    


def readWordFiles(arquivo:str):
    print(arquivo)
    print("Lendo arquivo {arquivo}")
    with open(file=arquivo, mode= "r", encoding = "utf-8") as palavras :
        
    


        print("Colhendo as palavras no arquivo")
        for linha in palavras:
            palavra = linha.strip()
            listOfWords.append(palavra)
            
        print("Finalzando a colheita")

    return len(listOfWords) 


def fillDataFrame():
    try:
        for i, word in enumerate(listOfWords):
            df.loc[i, "N"] = i
            df.loc[i, "Word"] = word 
            i += 1
            print(i)
                    
            if i > 100 :
                break

        df.head(5)
        return True 
    except Exception as e:
        print(f"Erro ao preencher o DataFrame: {e}")
        
        return False

def persistWords(): 
    print(df)
    arquivo = "cwh-{new_project}-{language}/db-{language}.xlsx".format(new_project=new_project, language = language)
    print("Persistir para : ")
    print(arquivo)
    df.to_excel(arquivo, engine="openpyxl")




def startNew(new_project, source, language, database):
    # criar uma pasta com o nome do valor em new_project
    os.mkdir("cwh-{new_project}-{language}".format(new_project=new_project, language=language))

    global df
    # criar um arquivo com o nome do valor em source
    df = loadDF(source)
    print(df)

    # Fazer a leitura dos arquivos de palavras
    numberOfWords = readWordFiles(source)

    print(numberOfWords)
    if (numberOfWords > 0):
        print("cha-mando filldataframe")
        isFilled = fillDataFrame()
        
        if isFilled:
            persistWords()
            print("Dados adicionados com sucesso!")
        else:
            print("Erro ao adicionar dados ao DataFrame.")


def startAdd(add_data, project_path):
    pass

def processArgs(args):
    global source, new_project, add_data, project_path, language, database
    # ✅ Acessando os valores dos argumentos
    source = args.source
    new_project = args.new
    add_data = args.add
    project_path = args.in_path
    language = args.lang
    database = args.dbname

    # ✅ Fazendo a manipulação baseada nos argumentos fornecidos
    if new_project:
        print(f"Criando novo projeto '{new_project}' com dados de '{source}'")
        # Código para criar um novo projeto...

    elif add_data:
        print(f"Adicionando dados de '{source}' ao projeto '{project_path}'")
        # Código para adicionar dados ao projeto existente...

    if language:
        print(f"Linguagem do projeto: {language}")

    if database:
        print(f"Nome do banco de dados: {database}")

    
    
    if args.new :
        startNew(new_project, source, language, database)
    else:
        startAdd(add_data, project_path)

def main():
    parser = argparse.ArgumentParser(description="Processamento de Projetos")

    parser.add_argument("--source", type=str, required=True, help="Caminho dos dados para criar um novo projeto")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--new", type=str, help="Nome da pasta gerada como projeto")
    group.add_argument("--add", action="store_true", help="Adicionar dados a um projeto existente")

    parser.add_argument("--in", type=str, dest="in_path", help="Caminho do projeto onde os dados serão adicionados")
    parser.add_argument("--lang", type=str, help="Linguagem do projeto")
    parser.add_argument("--dbname", type=str, help="Nome do banco de dados")

    args = parser.parse_args()

    # Validações adicionais
    if args.add and not args.in_path:
        parser.error("--add requer o argumento --in")
        exit
    
    if args.new and args.add:
        parser.error("--new e --add não podem ser usados juntos")
        exit

    processArgs(args)
    

if __name__ == "__main__":
    main()
