import random 
import os  
from functools import lru_cache
import csv
import re
from gtts import gTTS
import pygame
import tkinter as tk
from tkcalendar import Calendar
import datetime 
nome_arquivo = 'treinos.csv'

def registrar_treino():#pronto
    
    try:
        nome = input("Digite o seu nome: ").capitalize()
        data = input("Data do treino (dd/mm/aaaa): ")
        if validar_data(data):
                print("Data válida!")
        else:
             print("Data inválida.")
             return
        distancia = input("Distância total do evento (em km): ")
        if not distancia.replace('.', '', 1).isdigit() or float(distancia) <= 0:
                raise ValueError("A distância precisa ser um número positivo.")
                      
        tempo = input("Tempo total. formate assim (Ex: 23h59m): ")
        if validar_tempo_personalizado(tempo):
          print("Tempo válido!")
        else:
           print("Tempo inválido. Insira no formato correto (Ex: 23h59m).")
         
 
        pais = input("Digite o país: ").capitalize()
        paises = [
            "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bahrein", "Bélgica", "Belize", 
    "Benim", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", 
    "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", 
    "Chipre", "Colômbia", "Comores", "Congo", "Coréia do Norte", "Coréia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",
    "Dinamarca", "Djibouti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia", 
    "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", 
    "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", 
    "Haiti", "Honduras", "Hungria", "Iêmen", "Ilhas Marshall", "Ilhas Maurício", "Índia", "Indonésia", "Irã", "Iraque", 
    "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kosovo", "Kuwait",
    "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte", 
    "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Mauritânia", "México", "Mianmar", 
    "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal", "Nicarágua", 
    "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "Países Baixos", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", 
    "Paraguai", "Peru", "Polônia", "Portugal", "Quênia", "Quirguistão", "Reino Unido", "República Centro-Africana", "República Checa", "República Democrática do Congo",
    "República Dominicana", "Romênia", "Ruanda", "Rússia", "Samoa", "San Marino", "Santa Lúcia", "São Cristóvão e Nevis", 
    "São Tomé e Príncipe", "São Vicente e Granadinas", "Seicheles", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Síria", 
    "Somália", "Sri Lanka", "Sudão", "Sudão do Sul", "Suécia", "Suíça", "Suriname", "Tailândia", "Tajiquistão", "Tanzânia", 
    "Timor-Leste", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", 
    "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
]
        if pais not in paises:
          print("Erro: pais não existe inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( pais ))
          return
      
       
        cidade = input("Digite a cidade: ").capitalize()
        tipos_de_tempo =[
                              "Ensolarado",
                        "Chuvoso","Nublado","Tempestuoso", "Nevando",  "Ventoso", "Neblina", " Granizo","Garoa","Calor ","Frio ",
                        "Geada","Vento forte","Chuvisco","Chuva","Tempestade","Pancadas de chuva"
                      ]
        print(tipos_de_tempo)
        clima = input("Condições Tempo: ").capitalize()
        
        if clima not in tipos_de_tempo:
          print("Erro: Tipo de Clima inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( clima ))
          return
        arquivo_existe = os.path.isfile(nome_arquivo)

        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not arquivo_existe:
                writer.writerow(['Nome', 'Data', 'Distância (km)', 'Tempo', 'Localização', 'Clima', 'Tipo de Treino'])
            writer.writerow([nome, data, f'{distancia}Km', tempo,f'{cidade},{pais}', clima, 'Treino padrão'])

        print("Treino registrado com sucesso!\n")
    except ValueError :
        print("Erro: A distância precisa ser um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Aperte Enter pra continuar.")
       

def exibir_treinos_formatados(nome_arquivo):#pronto
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            dados = list(reader)
            
            if len(dados) <= 1:
                print("Nenhum treino registrado.")
                return
          
            cabecalho = ["Nome", "Data", "T.P.H/laps/km", "Tempo", "Localização", "Clima", "Tipo de Treino"]
            tamanhos_colunas = [10, 12, 15, 10, 20, 20, 20]  
        
            def formatar_linha(linha, tamanhos):
                return " | ".join([f"{coluna:<{tamanhos[i]}}" for i, coluna in enumerate(linha)])

           
            print(formatar_linha(cabecalho, tamanhos_colunas))
            
            print("-" * (sum(tamanhos_colunas) + 3 * (len(tamanhos_colunas) - 1))) 

            for linha in dados[1:]:
                print(formatar_linha(linha, tamanhos_colunas))

    except FileNotFoundError:
        print("Erro: Nenhum arquivo de treinos encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    input("Aperte Enter pra continuar:")
def filtrar_treinos():#pronto
    try:
        criterio = input("Deseja filtrar por 'distancia', 'tempo'? ").strip().lower()
        resultados = []

        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            linhas = list(reader)

            if len(linhas) <= 1:
                print("Nenhum treino registrado para filtrar.")
                return

            if criterio == 'distancia':
                distancia_min = float(input("Digite a distância mínima: "))
                for linha in linhas[1:]:
                    if float(linha[2]) >= distancia_min:
                        resultados.append(linha)
            elif criterio == 'tempo':
                tempo_max = input("Digite o tempo máximo (24h59m): ")
                for linha in linhas[1:]:
                    if linha[3] <= tempo_max:
                        resultados.append(linha)
            else:
                print("Critério inválido. Escolha 'distancia', 'tempo' ou 'voltas'.")
                return
        
        if resultados:
            print("\nTreinos filtrados:")
            for r in resultados:
                  print(f"| Nome: {r[0]}, Data: {r[1]}, Distância: {r[2]}, Tempo: {r[3]}, Localização: {r[4]}, Clima: {r[5]}, Tipo de Treino: {r[6]} |")
       
        else:
            print("Nenhum treino encontrado com esse critério.")
    except ValueError:
        print("Erro: Insira um valor numérico válido para o critério de filtro.")
    except FileNotFoundError:
        print("Erro: Nenhum arquivo de treinos encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("\nAperte Enter pra continuar:")


def salvar_meta():#pronto
    try:
        print("Escolha o período para a meta:")
        print("1 - Semanal")
        print("2 - Mensal")
        print("3 - Anual")
        opcao_periodo = int(input("Digite o número correspondente ao período da meta: "))
        
        if opcao_periodo == 1:
            periodo = 'semanal'
        elif opcao_periodo == 2:
            periodo = 'mensal'
        elif opcao_periodo == 3:
            periodo = 'anual'
        else:
            print("Opção inválida!")
            return
        
        meta_km = float(input("Digite a meta de km a serem percorridos: "))
        meta_voltas = int(input("Digite a meta de voltas: "))

        nome_arquivo_meta = 'metas.csv'
        with open(nome_arquivo_meta, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([periodo, meta_km, meta_voltas, datetime.date.today()])
        
        print(f"Meta de {periodo} salva com sucesso!")
    except ValueError:
        print("Erro: A meta de km ou voltas precisa ser um número válido.")

def verificar_meta():#pronto
    nome_arquivo_treinos = 'treinos.csv'
    nome_arquivo_meta = 'metas.csv'
    
    try:
        with open(nome_arquivo_meta, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            metas = list(reader)
            if not metas:
                print("Nenhuma meta salva para verificar.")
                return
            
            print("Escolha uma meta para verificar:")
            for i, meta in enumerate(metas, start=1):
                print(f"{i} - Período: {meta[0]}, Meta de km: {meta[1]}, Meta de voltas: {meta[2]}, Data: {meta[3]}")
            
            opcao_meta = int(input("Digite o número da meta que deseja verificar: ")) - 1
            if opcao_meta < 0 or opcao_meta >= len(metas):
                print("Opção inválida!")
                return
            
            periodo, meta_km, meta_voltas, data = metas[opcao_meta]
            meta_km = float(meta_km)
            meta_voltas = int(meta_voltas)
        
        total_km = 0
        total_voltas = 0
        with open(nome_arquivo_treinos, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            linhas = list(reader)

            if len(linhas) <= 1:
                print("Nenhum treino registrado para verificar metas.")
                return

            for linha in linhas[1:]:
                try:
                 
                    if "km" in linha[2].lower():
                        valor_km = linha[2].replace("Km", "").replace("km", "").strip()
                        total_km += float(valor_km)
                    elif "laps" in linha[2].lower():
                        valor_voltas = linha[2].replace("laps", "").strip()
                        total_voltas += int(valor_voltas)
                except ValueError:
                    print(f"Erro ao ler a linha: {linha}. Verifique o formato dos dados.")
            
            print(f"\nTotal de km percorridos: {total_km:.2f}")
            print(f"Total de voltas: {total_voltas}")

            if total_km >= meta_km:
                print("Meta de quilômetros atingida!")
            else:
                print(f"Faltam {meta_km - total_km:.2f} km para atingir a meta.")

            if total_voltas >= meta_voltas:
                print("Meta de voltas atingida!")
            else:
                print(f"Faltam {meta_voltas - total_voltas} laps para atingir a meta.")
                
    except ValueError:
        print("Erro: A meta de km ou voltas precisa ser um número válido.")
    except FileNotFoundError:
        print("Erro: Arquivo de treinos ou metas não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    input("Aperte Enter para continuar: ")

def sugestao_treinos(nome_arquivo):#pronto
    try:
        sugestoes = []

        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  
            for linha in reader:
                if linha:  
                    sugestoes.append(linha)

        if sugestoes:
            aleatorio = random.sample(sugestoes, min(6, len(sugestoes)))

            print("\n--- Sugestões de treino ---")
            for treino in aleatorio:
                nome = treino[0]
                data = treino[1]
                distancia = treino[2] if len(treino) > 2 else "N/A"
                tempo = treino[3] if len(treino) > 3 else "N/A"
                localizacao = treino[4] if len(treino) > 4 else "N/A"
                clima = treino[5] if len(treino) > 5 else "N/A"
                tipo_treino = treino[6] if len(treino) > 6 else "N/A"
                
                print(f"Nome: {nome}, Data: {data}, Distância: {distancia}, Tempo: {tempo}, Localização: {localizacao}, Clima: {clima}, Tipo de Treino: {tipo_treino}")
        else:
            print("Nenhum treino registrado para sugerir.")
            
    except FileNotFoundError:
        print("Erro: Nenhum arquivo de treinos encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    input("\nAperte Enter para continuar:")

def tipo_treino():#pronto
    modelo_carro = None
    potencia = None
    tracao = None
    transmissao = None
    tipo_combustivel = None
    marcar_carro = None 
    nome_arquivo = 'treinos.csv'
    combustivel = [
              "Gasolina", "Etanol", "Diesel", "GNV (Gás Natural Veicular)", "Elétrico",
               "Hidrogênio", "Biocombustíveis", "E85", "Propano (LPG - Gás Liquefeito de Petróleo)",
               "Metanol", "Óleo Vegetal Puro (SVO)", "Biogás", "Butanol", "Dimetiléter (DME)",
                "B100 (Biodiesel 100%)", "Hidrazina", "Nitroglicerina"
               ]
    tipos_transmissao = [
                              "Manual","Automática","Semi-automática","CVT", "Automatizada","DCT", "Tiptronic", "AMT",  "eCVT", "LST"                  
                                   ]
    especificacao_do_treino = "especificacao_do_treino.csv"
    
    try:
        opcoes_de_treino = ['Corrida de Kart', 'Corrida de Carro', 'Corrida de Rally', 'Corrida Virtual', 'Corrida de Moto']
        print("\n--- Tipos de Treino de Carro ---")

        for idx, opcao in enumerate(opcoes_de_treino, 1):
            print(f"{idx}. {opcao}")

        escolha = int(input("\nEscolha seu tipo de Treino (1-5): "))

        if 1 <= escolha <= 5:
            modoesporte = opcoes_de_treino[escolha - 1]
        else:
             print("Opção inválida.")
             return

        nome = input("Digite o seu nome: ")
        data = input("Data do treino (dd/mm/aaaa): ")
        if validar_data(data):
                print("Data válida!")
        else:
             print("Data inválida.")
             return
       
        voltas = input("Digite a quantidade de voltas (coloque no fim 'laps'): ")
        if float(voltas) <= 0:
                raise ValueError("A voltas precisa ser um número positivo.")
         
        tempo = input("Tempo total. formate assim(2h30m): ")
        if validar_tempo_personalizado(tempo):
          print("Tempo válido!")
        else:
           print("Tempo inválido. Insira no formato correto (Ex: 2h30m).")
        cidade = input("Digite a cidade: ").capitalize()
       
        pais = input("Digite o país: ").capitalize()
        paises = [
            "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bahrein", "Bélgica", "Belize", 
    "Benim", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", 
    "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", 
    "Chipre", "Colômbia", "Comores", "Congo", "Coréia do Norte", "Coréia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",
    "Dinamarca", "Djibouti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia", 
    "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", 
    "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", 
    "Haiti", "Honduras", "Hungria", "Iêmen", "Ilhas Marshall", "Ilhas Maurício", "Índia", "Indonésia", "Irã", "Iraque", 
    "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kosovo", "Kuwait",
    "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte", 
    "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Mauritânia", "México", "Mianmar", 
    "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal", "Nicarágua", 
    "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "Países Baixos", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", 
    "Paraguai", "Peru", "Polônia", "Portugal", "Quênia", "Quirguistão", "Reino Unido", "República Centro-Africana", "República Checa", "República Democrática do Congo",
    "República Dominicana", "Romênia", "Ruanda", "Rússia", "Samoa", "San Marino", "Santa Lúcia", "São Cristóvão e Nevis", 
    "São Tomé e Príncipe", "São Vicente e Granadinas", "Seicheles", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Síria", 
    "Somália", "Sri Lanka", "Sudão", "Sudão do Sul", "Suécia", "Suíça", "Suriname", "Tailândia", "Tajiquistão", "Tanzânia", 
    "Timor-Leste", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", 
    "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
]
        if pais not in paises:
          print("Erro: pais não existe inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( pais ))
          return
        tipos_de_tempo =[
                              "Ensolarado",
                        "Chuvoso","Nublado","Tempestuoso", "Nevando",  "Ventoso", "Neblina", " Granizo","Garoa","Calor extremo","Frio intenso","Lugar fechado"
                        "Geada","Neve derretendo","Vento forte","Chuvisco","Chuva de verão","Tempestade tropical","Brisa marítima","Pancadas de chuva","Tempestade de poeira"
                      ]
        print(tipos_de_tempo)
        clima = input("Condições climáticas: ")
        if clima not in tipos_de_tempo:
          print("Erro: Tipo de Clima inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( clima ))
        
        
        especificar= input("Você quer especificar os carros? (Sim/Não): ")
        
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nome, data, f'{voltas}Laps', tempo,f'{cidade},{pais}', clima, modoesporte])
            print("Treino registrado com sucesso!\n")
            
   
        if especificar.lower() in ['sim', 's','Sim','SIM','SS',"S"]:
            print("\n-- Detalhes da Corrida de Carro ou Moto --")
            marcar_carro = input("Marca do carro ou moto: ")
            modelo_carro = input("Modelo do carro ou moto: ")
            
            Tipo_motor = input("Digite o tipo de Motor: ")
            
            potencia = int(input("Potência do carro (em HP): "))
            if float(potencia) <= 0:
                raise ValueError("A Potência precisa ser um número positivo.")
       
            tracao = input("Tipo de tração (FWD, RWD, AWD): ").upper()
            if tracao not in ["FWD", "RWD", "AWD"]:
                print("Erro: Tipo de tração inválido.")
                return
            
            print(tipos_transmissao)  
            transmissao = input("Tipo de transmissão (Manual, Automática,Transmissão Automatizada (ou Semi-automática)e etc): ").capitalize()
            
            if transmissao not in tipos_transmissao:
                print("Erro: Tipo de transmissão inválido.")
                print("Escolha um dos seguintes tipos:", ", ".join(tipos_transmissao))
                return
            print(combustivel)
            tipo_combustivel = input("Tipo de combustível (Gasolina, Diesel, Elétrico, Híbrido,Etanol e etc): ").capitalize()
            
            if tipo_combustivel not in combustivel:
                print("Erro: Tipo de Combustivel inválido.")
                print("Escolha um dos seguintes tipos:", ", ".join( tipo_combustivel ))
                return
            if combustivel == "Hidrazina" "Nitroglicerina":
                print("Cuidado esses Dois combustiveis são muito perigos cuidado")
            
        try:
           if especificar.lower() in ['sim', 's','Sim','SIM','SS',"S"]:
             especificacao_do_treino = "data/especificacao_do_treino.csv"  
             
             
           with open(especificacao_do_treino, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    nome, modoesporte, marcar_carro, modelo_carro, f'{potencia}HP',
                    Tipo_motor, tracao, transmissao, tipo_combustivel
                ])
           print("Especificação do treino registrada com sucesso!\n")
        except Exception as e:
                print(f"Ocorreu um erro ao registrar o treino: {e}")
    except ValueError:
          print("Erro: Insira um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
   
def mode_esporte():#pronto
    nome_arquivo = 'treinos.csv'
    try:
        opcoes_de_treino = ['Ski na neve', 'Triathlon', 'Alpinismo', 'Natação', 'Maratona']
        print("\n--- Tipos de Treino ---")

        for idx, opcao in enumerate(opcoes_de_treino, 1):
            print(f"{idx}. {opcao}")

        escolha = int(input("\nEscolha seu tipo de Treino (1-5): "))

        if 1 <= escolha <= 5:
            modoesporte = opcoes_de_treino[escolha - 1]
        else:
            print("Opção inválida.")
            return
        nome = input("Digite o seu nome: ") 
        data = input("Data do treino (dd/mm/aaaa): ")
        if validar_data(data):
                print("Data válida!")
        else:
             print("Data inválida.")
             return
    
        km = input("Distância total do evento (em km): ")
        if not km.replace('.', '', 1).isdigit() or float(km) <= 0:
                raise ValueError("A distância precisa ser um número positivo.")
        
        tempo = input("Tempo total (Ex: 23h59m):")
        if validar_tempo_personalizado(tempo):
          print("Tempo válido!")
        else:
           print("Tempo inválido. Insira no formato correto (Ex: 23h59m).")
        
        cidade = input("Digite a cidade: ")
        
        pais = input("Digite o país: ")
        paises = [
            "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bahrein", "Bélgica", "Belize", 
    "Benim", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", 
    "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", 
    "Chipre", "Colômbia", "Comores", "Congo", "Coréia do Norte", "Coréia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",
    "Dinamarca", "Djibouti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia", 
    "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", 
    "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", 
    "Haiti", "Honduras", "Hungria", "Iêmen", "Ilhas Marshall", "Ilhas Maurício", "Índia", "Indonésia", "Irã", "Iraque", 
    "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kosovo", "Kuwait",
    "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte", 
    "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Mauritânia", "México", "Mianmar", 
    "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal", "Nicarágua", 
    "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "Países Baixos", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", 
    "Paraguai", "Peru", "Polônia", "Portugal", "Quênia", "Quirguistão", "Reino Unido", "República Centro-Africana", "República Checa", "República Democrática do Congo",
    "República Dominicana", "Romênia", "Ruanda", "Rússia", "Samoa", "San Marino", "Santa Lúcia", "São Cristóvão e Nevis", 
    "São Tomé e Príncipe", "São Vicente e Granadinas", "Seicheles", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Síria", 
    "Somália", "Sri Lanka", "Sudão", "Sudão do Sul", "Suécia", "Suíça", "Suriname", "Tailândia", "Tajiquistão", "Tanzânia", 
    "Timor-Leste", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", 
    "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
]
        if pais not in paises:
          print("Erro: pais não existe inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( pais ))
          return
            
        print(tipos_de_tempo)
        clima = input("Condições Tempo: ")
        tipos_de_tempo =[
                              "Ensolarado",
                        "Chuvoso","Nublado","Tempestuoso", "Nevando",  "Ventoso", "Neblina", " Granizo","Garoa","Calor extremo","Frio intenso",
                        "Geada","Neve derretendo","Vento forte","Chuvisco","Chuva de verão","Tempestade tropical","Brisa marítima","Pancadas de chuva","Tempestade de poeira"
                      ]
        if clima not in tipos_de_tempo:
          print("Erro: Tipo de Clima inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( clima ))
          return
      

        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nome, data,f'{km}km', tempo,f'{cidade},{pais}' , clima, modoesporte])
    
        print("Treino registrado com sucesso!\n")
    except ValueError:
        print("Erro: Insira um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Aperte Enter pra continuar.")
    
def menu_2():#Pronto
    nome_arquivo = 'treinos.csv'
    try:
        opcoes_de_treino = ['Calistenia', 'Musculação','Crossfit']
        print("\n--- Tipos de Treino Musculação---")

        for idx, opcao in enumerate(opcoes_de_treino, 1):
            print(f"{idx}. {opcao}")

        escolha = int(input("\nEscolha seu tipo de Treino (1-3): "))

        if escolha == 1:
            modoesporte = "Calistenia"
        elif escolha == 2:
            modoesporte = 'Musculação'
        elif escolha == 3:
            modoesporte = "Crossfit"
    
        else:    
            print("Opção inválida.")
            return
        nome = input("Digite o seu nome: ").capitalize() 
        data = input("Marque o dia do seu treino (dd/mm/aaaa): ")
        if validar_data(data):
                print("Data válida!")
        else:
             print("Data inválida.")
             return

        tipo_treino = input("Digite a parte do corpo como costas ou peito etc: ").capitalize()
        tempo = input("Tempo total. formate assim Ex:(2h30m): ")
        if validar_tempo_personalizado(tempo):
          print("Tempo válido!")
        else:
           print("Tempo inválido. Insira no formato correto (Ex: 2h30m).")
           return
        cidade = input("Digite a cidade: ")
       
        pais = input("Digite o país: ")
        paises = [
            "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bahrein", "Bélgica", "Belize", 
    "Benim", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", 
    "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", 
    "Chipre", "Colômbia", "Comores", "Congo", "Coréia do Norte", "Coréia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",
    "Dinamarca", "Djibouti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia", 
    "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", 
    "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", 
    "Haiti", "Honduras", "Hungria", "Iêmen", "Ilhas Marshall", "Ilhas Maurício", "Índia", "Indonésia", "Irã", "Iraque", 
    "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kosovo", "Kuwait",
    "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte", 
    "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Mauritânia", "México", "Mianmar", 
    "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal", "Nicarágua", 
    "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "Países Baixos", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", 
    "Paraguai", "Peru", "Polônia", "Portugal", "Quênia", "Quirguistão", "Reino Unido", "República Centro-Africana", "República Checa", "República Democrática do Congo",
    "República Dominicana", "Romênia", "Ruanda", "Rússia", "Samoa", "San Marino", "Santa Lúcia", "São Cristóvão e Nevis", 
    "São Tomé e Príncipe", "São Vicente e Granadinas", "Seicheles", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Síria", 
    "Somália", "Sri Lanka", "Sudão", "Sudão do Sul", "Suécia", "Suíça", "Suriname", "Tailândia", "Tajiquistão", "Tanzânia", 
    "Timor-Leste", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", 
    "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
]
        if pais not in paises:
          print("Erro: pais não existe inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( pais ))
          return
        print(tipos_de_tempo)
        clima = input("Condições Tempo: ")
        tipos_de_tempo =[
                              "Ensolarado",
                        "Chuvoso","Nublado","Tempestuoso", "Nevando",  "Ventoso", "Neblina", " Granizo","Garoa","Calor","Frio",
                        "Geada","Neve derretendo","Vento forte","Chuvisco","Chuva","Lugar fechado"
                      ]
        if clima not in tipos_de_tempo:
          print("Erro: Tipo de Clima inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( clima ))
          return
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nome,data,tipo_treino , tempo,f'{cidade},{pais}', clima, modoesporte])
        print("Treino registrado com sucesso!\n")
    except ValueError:
        print("Erro: Insira um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def excluir():#pronto
    try: 
        opcoes_de_treino = ['Treinos', 'Especificação', 'Competição','Metas']
        print("\n--- Tipos de Excluir ---")
        print(opcoes_de_treino)

        escolha = int(input("\nEscolha o tipo de treino para excluir (1 a 4): "))

        if escolha not in [1, 2, 3,4]:
            print("Opção inválida.")
            return

        if escolha == 1:
            nome_arquivo = 'treinos.csv'
        elif escolha == 2:
            nome_arquivo = 'especificacao_do_treino.csv'
        elif escolha == 3:
            nome_arquivo = 'competicoes.csv'
        elif escolha == 4:
           nome_arquivo='metas.csv'
        nome_treino = input("Digite o nome da pessoa que deseja excluir o treino: ")

      
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            linhas = list(csv.reader(file))

       
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            linha_excluida = False
            for linha in linhas:
                if linha[0].lower() == nome_treino.lower():  
                    confirmacao = input(f"Tem certeza de que deseja excluir '{nome_treino}'? (s/n): ").lower()
                    if confirmacao == 's':
                        print(f"'{nome_treino}' excluído com sucesso.")
                        linha_excluida = True
                    else:
                        writer.writerow(linha)
                else:
                    writer.writerow(linha)

            if not linha_excluida:
                print(f"'{nome_treino}' não encontrado no arquivo '{nome_arquivo}'.")

    except FileNotFoundError:
        print("Erro: Nenhum arquivo encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
def manual_do_usuario():#Pronto
    print("\n--- Manual do Usuário ---")
    print("Escolha como você quer visualizar o manual: ")
    print("1. Exibir no console")
    print("2. Baixar em arquivo de texto")
    print("3. Escute o áudio do texto em PT-Br")
    
    try:
        
        explicar = int(input("\nEscolha uma opção (1 a 3): "))

        if explicar == 1:
            print("--- Manual do Usuário ---")
            print("----- Introdução -----")
            print("Este sistema permite o cadastro e gerenciamento de treinos e competições, oferecendo funções para registrar, visualizar, e acompanhar treinos, além de estabelecer e monitorar metas pessoais.\n")

            print("Pré-requisitos:")
            print("- Python 3 instalado")
            print("- Bibliotecas integradas: csv, os, calendar e random\n")

            print("----- Iniciando o Sistema -----")
            print("1. Abra o terminal ou prompt de comando.")
            print("2. Navegue até o diretório onde o código está salvo.")
            print("3. Execute o comando: python nome_do_arquivo.py\n")

            print("----- Opções do Menu -----")
            print("\n--- Sistema de Cadastro de Treinos e Competições ---")
            print("1. Registrar treino/competição")
            print("2. Exibir todos os treinos/competições")
            print("3. Filtrar treinos por distância ou tempo")
            print("4. Verificar metas")
            print("5. Sugerir treinos aleatórios")
            print("6. Registrar o Genêro de Corrida")
            print("7. Modo Esporte")
            print("8. Treino Musculação")
            print("9. Calendario")
            print("10. Excluir treinos")
            print("11. Manual do usuário")
            print("12. Rank")
            print('13. Registre uma competição ')
            print("14. Sair")

            print("----- Dicas de Uso -----")
            print("Insira a data e o tempo no formato correto.")
            print("Ao excluir, verifique os dados para evitar exclusões acidentais.\n")
            input("Aperte Enter pra continuar:")
        elif explicar == 2:
            manual_usuario = """
            ----- Manual do Usuário -----

            ----- Introdução -----
            Este sistema permite o cadastro e gerenciamento de treinos e competições...

            ----- Pré-requisitos -----
            - Python 3 instalado
            - Bibliotecas integradas: csv, os, calendar e random

            ----- Iniciando o Sistema -----
            1. Abra o terminal ou prompt de comando.
            2. Navegue até o diretório onde o código está salvo.
            3. Execute o comando: python nome_do_arquivo.py

            ----- Opções do Menu -----
            1. Registrar Treino ou Competição
            2. Exibir Todos os Treinos
            3. Filtrar Treinos
            4. Verificar Metas
            5. Sugerir Treinos Aleatórios
            6. Registrar Tipo de Treino Específico
            7. Modo Esporte
            8. Treino Musculação
            9. Calendário
            10.Excluir Treino 
            11.Manual do usuário
            12.Rank
            13.Registre uma competição 
            14.Sair 

            ----- Dicas de Uso -----
            Insira a data e o tempo no formato correto.
            Ao excluir, verifique os dados para evitar exclusões acidentais.

            ----- Fim do Manual -----
            """
            
            with open("manual_usuario.txt", "w", encoding="utf-8") as file:
             file.write(manual_usuario)
             os.makedirs("/mnt/data", exist_ok=True)

            with open("/mnt/data/manual_usuario.txt", "w", encoding="utf-8") as file:
              file.write(manual_usuario)
            print("\nManual salvo com sucesso! Acesse o arquivo: /mnt/data/manual_usuario.txt"  ) 
            input("Aperte Enter pra continuar:") 

        elif  explicar == 3:
            manual_texto = """
                Manual do Usuário - Sistema de Treinos e Competições

             Introdução:
             Este sistema permite o cadastro e gerenciamento de treinos e competições, oferecendo funções para registrar, visualizar, e acompanhar treinos, além de estabelecer e monitorar metas pessoais.

             Pré-requisitos:
             É necessário que você tenha o Python 3 instalado, além das bibliotecas integradas: csv, os, calendar e random.

             Iniciando o Sistema:
             1. Abra o terminal ou prompt de comando.
             2. Navegue até o diretório onde o código está salvo.
             3. Execute o comando: python nome_do_arquivo.py

           Opções do Menu:
             1. Registrar Treino ou Competição - Aqui, você pode registrar dados como nome, data, distância, tempo, localização e clima.
             2. Exibir Todos os Treinos - Visualize todos os treinos registrados em formato de tabela.
             3. Filtrar Treinos - Filtre treinos por distância mínima, tempo máximo ou voltas.
             4. Verificar Metas - Defina uma meta de quilômetros a percorrer e acompanhe seu progresso.
             5. Sugerir Treinos Aleatórios - Receba sugestões aleatórias de treino com base nos registros existentes.
             6. Registrar Tipo de Treino Específico - Escolha entre várias modalidades de corrida e veículos.
             7. Modo Esporte - Selecione entre Ski, Triathlon, Alpinismo, Natação, entre outros.
             8. Treino Musculação - Registre treinos de Calistenia, Musculação ou Crossfit.
             9. Calendário - Consulte o calendário de um mês específico.
             10.Excluir Treino - Exclua um treino específico fornecendo o nome.
             11.Manual do usuário
             12.Rank
             13.Registre uma competição -  Aqui, você pode registrar dados como nome, data, distância, tempo, localização e clima no seu evento.
             14.Sair - Encerra o sistema.
            Dicas de Uso:
            Verifique sempre o formato de data e tempo ao inserir informações.
            Antes de excluir, certifique-se dos dados para evitar exclusões acidentais.

            Mensagens de Erro:
             Em caso de erro, o sistema exibe uma mensagem orientando sobre o problema.

             Fim do Manual. Aproveite o sistema!
               """
            tts =gTTS(text=manual_texto, lang='pt')
            audio_path = "manual_audio.mp3"
        
            tts.save(audio_path)
            
            pygame.mixer.init()

            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                  pygame.time.Clock().tick(20)
        
            print("Aguarde uns minutos pra escutar o áudio : ")
          
        else:
         print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro: Insira um número válido.")
    input("Aperte Enter pra continuar:")

def registrar_competicao(nome_arquivo):#pronto
    nome_arquivo = "competicoes.csv"
    quantidade=0
    try:
        opcoes_de_competicao = ['Competição de corrida normal', 'Corrida de carro']
        print("\n--- Competição ---")

        for idx, opcao in enumerate(opcoes_de_competicao, 1):
            print(f"{idx}. {opcao}")

        escolha = int(input("\nEscolha o tipo de competição (1 ou 2): "))

        if escolha not in [1, 2]:
            print("Opção inválida.")
            return

        arquivo_existe = os.path.isfile(nome_arquivo)

        if escolha == 1 :
            opcoes_de_corrida = ['Ski na neve', 'Triathlon', 'Alpinismo', 'Natação', 'Maratona', 'Atletismo']
            print(opcoes_de_corrida)  
            modoesporte =input("Digite uma das modalidades: ")
        
        if escolha ==2:
            opcoes_de_corrida = ['Corrida de Kart', 'Corrida de Carro', 'Corrida de Rally', 'Drag Race', 'Corrida de Moto',"Corrida virtual"]
            print(opcoes_de_corrida)
            modoesporte =input("Digite uma das modalidades: ")
            if modoesporte not in opcoes_de_corrida:
                print("Erro: Tipo de categoria inválido.")
                print("Escolha um dos seguintes tipos:", ", ".join(opcoes_de_corrida))
                return
        if escolha == 1 or 2 :
         nome = input("Digite o nome do Evento: ").capitalize()
         data = input("Data do evento (dd/mm/aaaa): ")
        if validar_data(data):
                print("Data válida!")
        else:
             print("Data inválida.")
             return
        if escolha ==1 :
             distancia = input("Distância total do evento (em km): ")
        if not distancia.replace('.', '', 1).isdigit() or float(distancia) <= 0:
                raise ValueError("A distância precisa ser um número positivo.")
        if escolha ==2:
             distancia = input("Distância total do evento (em Voltas): ")
        if not distancia.replace('.', '', 1).isdigit() or float(distancia) <= 0:
                raise ValueError("A distância precisa ser um número positivo.")

        if escolha == 1 or 2 :
         tempo = input("Tempo total do evento (hh:mm:ss): ")
         if validar_tempo_personalizado(tempo):
             print("Tempo válido!")
         else:
             print("Tempo inválido. Insira no formato correto (Ex: 2h30m).")
        if escolha == 1 or 2 :
          cidade = input("Digite a cidade onde começa o evento: ").capitalize()
          pais = input("Digite o país do evento: ").capitalize()
  
          tipos_de_tempo = [
                "Ensolarado", "Chuvoso", "Nublado", "Tempestuoso", "Nevando", "Ventoso", "Neblina", "Granizo",
                "Garoa", "Calor extremo", "Frio intenso", "Geada", "Neve Derretendo", "Vento Forte", "Chuvisco",
                "Chuva De verão", "Tempestade tropical", "Brisa marítima", "Pancadas De Chuva", "Tempestade De Poeira"
            ]
          print(tipos_de_tempo)
          clima = input("Condições climáticas do evento: ").capitalize()

        if clima not in tipos_de_tempo:
                print("Erro: Tipo de Clima inválido.")
                print("Escolha um dos seguintes tipos:", ", ".join(tipos_de_tempo))
                return

        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if not arquivo_existe:
                    writer.writerow(['Nome', 'Data', 'Distância(km e laps)', 'Tempo', 'Localização', 'Clima', 'Tipo de competição',])
                writer.writerow([nome, data,f'{distancia}km ou laps', tempo, f'{cidade},{pais}', clima, modoesporte,quantidade])

        print("Competição registrada com sucesso!\n")

    except ValueError:
        print("Erro: A distância precisa ser um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Aperte Enter pra continuar:")

def exibir_competição(nome_arquivo):#pronto

   nome_arquivo = "competicoes.csv"
   try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            dados = list(reader)

            if len(dados) <= 1:
                print("Nenhuma competição registrado.")
                return

            cabecalho = ["Nome", "Data", "laps/km", "Tempo", "Localização", "Clima","Competição","Participante"]
            tamanhos_colunas = [20, 12, 10, 10, 20, 15, 12, 15]  

            def formatar_linha(linha, tamanhos):
                return " | ".join([f"{coluna:<{tamanhos[i]}}" for i, coluna in enumerate(linha)])

            
            print(formatar_linha(cabecalho, tamanhos_colunas))
            print("-" * (sum(tamanhos_colunas) + 3 * (len(tamanhos_colunas) - 1))) 

            for linha in dados[1:]:
                print(formatar_linha(linha, tamanhos_colunas))

   except FileNotFoundError:
        print("Erro: Nenhum arquivo de treinos encontrado.")
   except Exception as e:
        print(f"Erro inesperado: {e}")

   input("Aperte Enter pra continuar:")

def corrida_Curta():#Pronto
    nome_arquivo = 'treinos.csv'
    especificacao_do_treino = "especificacao_do_treino.csv"
    tipos_de_tempo = [
        "Ensolarado", "Chuvoso", "Nublado","Nevando", "Ventoso",
        "Neblina", "Garoa", "Calor", "Frio intenso",
        "Neve", "Vento forte", "Chuvisco"
    ]
    tipos_transmissao = [
        "Manual", "Automática", "Semi-automática", "CVT", "Automatizada",
        "DCT", "Tiptronic", "AMT", "eCVT", "LST"
    ]
    combustivel = [
        "Gasolina", "Etanol", "Diesel", "GNV (Gás Natural Veicular)", "Elétrico",
        "Hidrogênio", "Biocombustíveis", "E85", "Propano (LPG - Gás Liquefeito de Petróleo)",
        "Metanol", "Óleo Vegetal Puro (SVO)", "Biogás", "Butanol", "Dimetiléter (DME)",
        "B100 (Biodiesel 100%)", "Hidrazina", "Nitroglicerina"
    ]

    try:
        opcoes_de_treino = ['Drag race', 'Atletismo']
        print("\n--- Tipos de Treino Curtas---")
        for idx, opcao in enumerate(opcoes_de_treino, 1):
            print(f"{idx}. {opcao}")
        escolha = int(input("\nEscolha seu tipo de Treino (1-2): "))

        if 1 <= escolha <= 2:
            modoesporte = opcoes_de_treino[escolha - 1]
        else:
            print("Opção inválida.")
            return

        nome = input("Digite o seu nome: ").capitalize()
        data = input("Data do treino (dd/mm/aaaa): ")
        if not validar_data(data):
            print("Data inválida.")
            return

        km = int(input("Distância total do evento (em Metros): "))
        if km <= 0:
            print("A distância precisa ser um número positivo.")
            return
        if km >= 3000:
            print("Para distâncias maiores que 3Km, use a parte de Treinos.")
            return

        tempo = input("Tempo total (Ex: 23h59m): ")
        if not validar_tempo_personalizado(tempo):
            print("Tempo inválido. Insira no formato correto (Ex: 2h30m).")
            return

        cidade = input("Digite a cidade: ").capitalize()
        pais = input("Digite o país: ").capitalize()
        paises = [
            "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita", "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bahrein", "Bélgica", "Belize", 
    "Benim", "Bielorrússia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", 
    "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", 
    "Chipre", "Colômbia", "Comores", "Congo", "Coréia do Norte", "Coréia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba",
    "Dinamarca", "Djibouti", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovênia", 
    "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", 
    "Gâmbia", "Gana", "Geórgia", "Granada", "Grécia", "Guatemala", "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", 
    "Haiti", "Honduras", "Hungria", "Iêmen", "Ilhas Marshall", "Ilhas Maurício", "Índia", "Indonésia", "Irã", "Iraque", 
    "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Kiribati", "Kosovo", "Kuwait",
    "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Macedônia do Norte", 
    "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Mauritânia", "México", "Mianmar", 
    "Micronésia", "Moçambique", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Namíbia", "Nauru", "Nepal", "Nicarágua", 
    "Níger", "Nigéria", "Noruega", "Nova Zelândia", "Omã", "Países Baixos", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", 
    "Paraguai", "Peru", "Polônia", "Portugal", "Quênia", "Quirguistão", "Reino Unido", "República Centro-Africana", "República Checa", "República Democrática do Congo",
    "República Dominicana", "Romênia", "Ruanda", "Rússia", "Samoa", "San Marino", "Santa Lúcia", "São Cristóvão e Nevis", 
    "São Tomé e Príncipe", "São Vicente e Granadinas", "Seicheles", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Síria", 
    "Somália", "Sri Lanka", "Sudão", "Sudão do Sul", "Suécia", "Suíça", "Suriname", "Tailândia", "Tajiquistão", "Tanzânia", 
    "Timor-Leste", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turcomenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", 
    "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Zâmbia", "Zimbábue"
]
        if pais not in paises:
          print("Erro: pais não existe inválido.")
          print("Escolha um dos seguintes tipos:", ", ".join( pais ))
          return
        
        print("Opções de condições de tempo:", ", ".join(tipos_de_tempo))
        clima = input("Condições do Tempo: ").capitalize()
        if clima not in tipos_de_tempo:
            print("Erro: Tipo de Clima inválido.")
            return
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nome, data, f'{km}M', tempo, f'{cidade},{pais}', clima, modoesporte])
        print("Treino registrado com sucesso!\n")

        if escolha ==1 :
         especificar = input("Você quer especificar os carros? (Sim/Não): ").strip().lower()
        if especificar in ['sim', 's','Sim','SIM','SS',"S"]:
            marcar_carro = input("Marca do carro ou moto: ").capitalize()
            modelo_carro = input("Modelo do carro ou moto: ").capitalize()
            tipo_motor = input("Digite o tipo de motor: ").capitalize()
            potencia = int(input("Potência do carro (em HP): "))

            tracao = input("Tipo de tração (FWD, RWD, AWD): ").upper()
            if tracao not in ["FWD", "RWD", "AWD"]:
                print("Erro: Tipo de tração inválido.")
                return

            transmissao = input("Tipo de transmissão (Manual, Automática, etc): ")
            if transmissao not in tipos_transmissao:
                print("Erro: Tipo de transmissão inválido.")
                return

            tipo_combustivel = input("Tipo de combustível (Gasolina, Diesel, etc): ")
            if tipo_combustivel not in combustivel:
                print("Erro: Tipo de Combustível inválido.")
                return

          
            with open(especificacao_do_treino, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    nome, modoesporte, marcar_carro, modelo_carro, f'{potencia}HP',tipo_motor, tracao, transmissao, tipo_combustivel
                ])
            print("Especificação do treino registrada com sucesso!\n")

    except ValueError:
        print("Erro: Insira um número válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Aperte Enter pra continuar:")
def registre_sua_presença(nome_arquivo):#pronto
    
    nome_arquivo = "competicoes.csv"
    try:
        if not os.path.isfile(nome_arquivo):
            print("Erro: Nenhum arquivo de competições encontrado.")
            return
        
        nome_evento = input("Digite o nome do evento para registrar presença: ")

        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            dados = list(reader)
     
        index_evento = None
        for i, linha in enumerate(dados):
            if i > 0 and linha[0].strip().lower() == nome_evento.strip().lower():
                index_evento = i
                break

        if index_evento is None:
            print("Erro: Evento não encontrado.")
            return

        participantes = dados[index_evento][-1]  
        if participantes.isdigit():
            dados[index_evento][-1] = str(int(participantes) + 1)
        else:
            dados[index_evento][-1] = "1"
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(dados)

        print(f"Presença registrada para o evento '{nome_evento}'. Total de participantes: {dados[index_evento][-1]}")

    except Exception as e:
        print(f"Erro inesperado: {e}")
    input("Aperte Enter pra continuar.")
def validar_data(data):#pronto
    from datetime import datetime
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False
def validar_tempo_personalizado(tempo):#pronto
    
    padrao = r"^(\d{1,2})h(\d{1,2})m$"
    match = re.match(padrao, tempo)

    if match:
        horas = int(match.group(1))
        minutos = int(match.group(2))
        
       
        if 0 <= horas <= 23 and 0 <= minutos <= 59:
            return True

    return False

def carregar_eventos(calendario, arquivos):#pronto
    for nome_arquivo in arquivos:
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for linha in reader:
                    data = linha[1]
                    try:
                        dia, mes, ano = map(int, data.split('/'))
                        data_evento = datetime.date(ano, mes, dia)
                       
                        tipo_evento = 'Treino' if 'treinos' in nome_arquivo else 'Competição'
                        calendario.calevent_create(data_evento, tipo_evento, tipo_evento.lower())
                    except ValueError:
                        print(f"Erro: Data inválida encontrada no arquivo - {data}")
        except FileNotFoundError:
            print(f"Erro: Arquivo {nome_arquivo} não encontrado.")

def exibir_detalhes_evento(eventos, calendario, label_evento):
   
    data_selecionada = calendario.selection_get()
    eventos = calendario.get_calevents(data_selecionada)
    
    if eventos:
        evento_info = [calendario.calevent_cget(e, "text") for e in eventos]
        label_evento.config(text=f"Eventos para {data_selecionada}: {', '.join(evento_info)}")
    else:
        label_evento.config(text=f"Sem eventos para {data_selecionada}")

def mostrar_calendario():#Pronto
    
    janela_calendario = tk.Tk()
    janela_calendario.title("Calendário de Eventos e Treinos")

    calendario = Calendar(
        janela_calendario,
        selectmode='day',
        year=datetime.datetime.now().year,
        month=datetime.datetime.now().month,
        day=datetime.datetime.now().day
    )
    calendario.pack(pady=10)
    
    calendario.tag_config('Competição', background='red', foreground='black')
    
    calendario.tag_config('treino', background='purple', foreground='white')
   
   
    arquivos = ['treinos.csv', 'competicoes.csv']
    carregar_eventos(calendario, arquivos)
    
    label_evento = tk.Label(janela_calendario, text="Selecione uma data para ver os eventos", font=("pacifico", 8))
    label_evento.pack(pady=10)
    
    calendario.bind("<<CalendarSelected>>", lambda e: exibir_detalhes_evento(e, calendario, label_evento))
    
    btn_fechar = tk.Button(janela_calendario, text="Fechar", command=janela_calendario.destroy)
    btn_fechar.pack(pady=10)
    janela_calendario.mainloop(1)
mostrar_calendario()
def calcular_diferenca(peso_inicial, peso_atual):
    
    return peso_inicial - peso_atual

def calcular_diferenca(peso_inicial, peso_atual):
    return peso_inicial - peso_atual

def calcular_percentual_perda(peso_inicial, perda_peso):
    if perda_peso > 0:
        return (perda_peso / peso_inicial) * 100
    return None

def calcular_peso_ideal(sexo, altura_cm):
    altura_in = altura_cm / 2.54
    if sexo.lower() == 'masculino':
        return 50 + 2.3 * (altura_in - 60)
    elif sexo.lower() == 'feminino':
        return 45.5 + 2.3 * (altura_in - 60)
    else:
        return None

def salvar_resultado(nome, perda_peso, percentual_perda):
    nome_arquivo = "perda_peso.csv"
    with open(nome_arquivo, "w", newline='', encoding='utf-8') as arquivo:
        if percentual_perda is not None:
            arquivo.write(f"{nome}, a sua perda de peso foi de: {perda_peso:.2f} kg\n")
            arquivo.write(f"O percentual de perda de peso foi: {percentual_perda:.2f}%\n")
        else:
            arquivo.write(f"{nome}, não existe perda de peso\n")
    print("Os resultados foram salvos no arquivo.")

def main():
    nome = input('Digite seu nome: ')
    sexo = input("Digite seu sexo (masculino ou feminino): ").strip().lower()
    
    if sexo not in ['masculino', 'feminino']:
        print("Sexo inválido. Escolha 'masculino' ou 'feminino'.")
        return

    altura_cm = float(input("Digite sua altura em centímetros: "))
    peso_ideal = calcular_peso_ideal(sexo, altura_cm)
    
    if peso_ideal:
        print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

    peso_inicial = float(input('Digite o seu peso inicial (por exemplo, o peso do início do ano passado): '))
    peso_atual = float(input('Digite seu peso atual: '))
    
    balha= input('Você é sedentario ? ')
    if balha in ['sim', 's','Sim','SIM','SS',"S"]:
         print('Qual é seu nivel de Sedentarismo :')
         print("Nível 1: A pessoa se movimenta, mas não pratica exercícios de média intensidade")
         print("Nível 2: A pessoa pratica algum tipo de atividade física, mas de forma esporádica")
         print("Nível 3: A pessoa evita qualquer tipo de esforço físico")
         print("Nível 4: O nível mais grave, em que a pessoa passa muito tempo sentada ou deitada")
    escolha=int(input("Digite seu Nivel :"))
    if escolha == 1 :
           print("Você estar no Nível 1 :")
           print(
    "1. Inicie com Movimentos Simples: Tente adicionar pequenas atividades ao longo do dia. "
    "Por exemplo, levante-se a cada 30 minutos para alongar-se ou dar uma breve caminhada. "
    "Suba escadas em vez de usar o elevador, ou faça uma caminhada curta depois das refeições.",
    
    "2. Estabeleça Metas Realistas: Comece com metas pequenas, como caminhar 10 minutos por dia e, com o tempo, "
    "aumente o tempo ou intensidade. Tente atingir, ao longo das semanas, pelo menos 150 minutos de atividade física "
    "moderada por semana (pode ser distribuído em 30 minutos por dia, cinco vezes na semana).",
    
    "3. Adicione Exercícios de Força: Exercícios simples, como agachamentos ou flexões, podem ser feitos em casa e "
    "ajudam a fortalecer os músculos. Use garrafas de água como pesos leves ou elásticos de resistência para facilitar os exercícios.",
    
    "4. Transforme em Hábito: Faça da atividade física parte da sua rotina, seja indo a pé a lugares próximos ou fazendo pausas "
    "ativas ao longo do dia. Defina horários específicos para se exercitar e trate esses momentos como compromissos.",
    
    "5. Use Aplicativos ou Contadores de Passos: Aplicativos de monitoramento de passos ou saúde podem ajudar a medir seu progresso "
    "e mantê-lo motivado. Uma meta inicial pode ser 5.000 passos diários, e aos poucos tentar alcançar 10.000.",
    
    "6. Procure Atividades que Gosta: Experimente diferentes tipos de atividades, como dança, bicicleta, natação, ou mesmo "
    "jardinagem, para tornar o movimento mais agradável.",
    
    "7. Envolva Amigos ou Família: Atividades em grupo, como caminhadas com amigos, podem tornar o exercício mais divertido e motivador.")
           input("\nAperte Enter pra continuar:")
    elif escolha==2 :
        print("Você estar no Nível 2 :")
        print(
         "1. Aumente a Frequência das Atividades: Tente incluir caminhadas diárias de 20 a 30 minutos, cinco vezes por semana, "
    "para construir uma rotina de atividade física moderada.",

    "2. Planeje Exercícios Aeróbicos Semanais: Pratique atividades que elevem a frequência cardíaca, como caminhadas rápidas, "
    "bicicleta ou natação, buscando acumular pelo menos 150 minutos de atividade física moderada por semana.",

    "3. Incorpore Exercícios Funcionais: Movimentos como agachamentos, elevação de joelhos e flexões são simples, mas eficazes "
    "para fortalecer o corpo. Faça pequenas séries ao longo do dia para criar condicionamento físico.",

    "4. Use Metas e Ferramentas de Monitoramento: Estabeleça metas pequenas e utilize aplicativos ou dispositivos que monitorem "
    "passos ou calorias queimadas, aumentando as metas aos poucos para melhorar o desempenho.",

    "5. Integre Atividades Físicas à Rotina: Escolha atividades prazerosas que possam ser realizadas com frequência, como "
    "jardinagem, dança ou caminhadas ao ar livre, para tornar a prática mais natural e divertida.",

    "6. Adote uma Rotina de Alongamentos: Faça pausas para alongamentos durante o dia, ajudando a evitar dores musculares e "
    "aumentando a flexibilidade. Isso também ajuda na disposição para outras atividades.",

    "7. Experimente Atividades ao Ar Livre: Explore parques ou áreas abertas para caminhar ou correr, o que ajuda a tornar "
    "a prática física mais prazerosa e pode reduzir o estresse.")
        input("\nAperte Enter pra continuar:")
    elif escolha==3 :
        print("Você estar no Nível 3 :")
        print(
           "1. Aumente a Intensidade dos Exercícios: Se você já realiza atividades leves, tente incorporar exercícios de intensidade moderada, "
    "como caminhada rápida, ciclismo ou dança. Procure alcançar uma frequência cardíaca que indique um esforço moderado, ideal para melhorias de condicionamento.",

    "2. Crie uma Rotina de Exercícios Consistente: Busque estabelecer uma frequência regular, exercitando-se pelo menos três a cinco vezes por semana. "
    "Essa constância ajuda a consolidar o hábito e a melhorar gradualmente a condição física.",

    "3. Adicione Treinos Intervalados: Experimente treinos intervalados (HIIT) – alternando períodos de atividade intensa com recuperação ativa. "
    "Esses treinos são ótimos para melhorar a resistência e o condicionamento cardiovascular em um tempo menor.",

    "4. Monitore seu Progresso: Utilize aplicativos ou dispositivos de monitoramento de saúde para acompanhar sua evolução. Defina metas de progresso, "
    "como aumentar a duração ou a intensidade dos treinos a cada semana.",

    "5. Inclua Exercícios de Força Regularmente: Se você faz atividades aeróbicas, acrescente exercícios de resistência, como levantamento de peso ou "
    "exercícios com elásticos. Eles são essenciais para fortalecer os músculos e proteger as articulações.",

    "6. Varie as Atividades: Evite a monotonia alterando suas atividades físicas. Experimente novas modalidades")