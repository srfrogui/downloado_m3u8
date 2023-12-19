import os
import re
import subprocess

# Função para solicitar uma escolha ao usuário
def solicitar_escolha(mensagem, opcoes):
    print(mensagem)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    while True:
        escolha = input(f"Digite sua escolha (1-{len(opcoes)}): ")
        if re.match(r"^\d+$", escolha) and 1 <= int(escolha) <= len(opcoes):
            return opcoes[int(escolha) - 1]
        
# Função para imprimir texto com cor
def imprimir_com_cor(texto, cor):
    cores = {
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'reset': '\033[0m'
    }
    reset = cores['reset']
    
    if cor in cores:
        cor_selecionada = cores[cor]
        print(f"{cor_selecionada}{texto}{reset}")
    else:
        print(texto)

# Solicitar URL do vídeo ao usuário
video_url = input("Digite a URL do vídeo (m3u8): ")

# Perguntar se o usuário deseja o vídeo completo ou segmentos específicos
escolha = solicitar_escolha("Você quer o vídeo completo ou segmentos específicos?", ["Vídeo Completo", "Segmentos Específicos"])
destino = input("Digite o caminho completo para o diretório de destino: ")

if escolha == "Vídeo Completo":
    # Se o usuário desejar o vídeo completo, perguntar apenas o formato de saída
    escolha_formato_saida = solicitar_escolha("Escolha o formato de saída:", ["AVI", "MP4", "MKV", "MP3", "Outro"])
    if escolha_formato_saida == "Outro":
        formato_saida = input("Digite o formato de saída desejado (por exemplo, 'mov', 'flv', etc.): ")
    else:
        formato_saida = escolha_formato_saida.lower()
    nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
    saida = f"{nome_arquivo_saida}.{formato_saida}"

    # Caminho completo para o arquivo de saída
    caminho_saida = os.path.join(destino, saida)
    imprimir_com_cor(f"ffmpeg.exe -i {video_url} -c copy \"{caminho_saida}\"\n", 'amarelo')
    comando = f"ffmpeg.exe -i {video_url} -c copy \"{caminho_saida}\""
    imprimir_com_cor(f"Baixando o vídeo completo para {caminho_saida}...\n", 'amarelo')
    subprocess.run(comando, shell=True)
    imprimir_com_cor(f"Download concluído: {caminho_saida}\n", 'verde')

else:
    # Se o usuário desejar segmentos específicos, perguntar o horário de início, fim e outras informações para cada segmento
    segmentos = []
    while True:
        horario_inicio = input("Digite o horário de início do segmento (formato: HH:mm:ss): ")
        horario_fim = input("Digite o horário de fim do segmento (formato: HH:mm:ss): ")
        nome_arquivo_saida = input("Digite o nome do arquivo de saída para o segmento (sem extensão): ")
        escolha_formato_saida = solicitar_escolha("Escolha o formato de saída para este segmento:", ["AVI", "MP4", "MKV", "MP3", "Outro"])

        if escolha_formato_saida == "Outro":
            formato_saida = input("Digite o formato de saída para este segmento (por exemplo, 'mov', 'flv', etc.): ")
        else:
            formato_saida = escolha_formato_saida.lower()

        saida = f"{nome_arquivo_saida}.{formato_saida}"

        # Construa o caminho completo para o arquivo de saída
        caminho_saida = os.path.join(destino, saida)

        segmentos.append({
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
            "nome_arquivo_saida": caminho_saida,  # Use o caminho completo
        })

        adicionar_mais_escolha = solicitar_escolha("Deseja adicionar mais segmentos?", ["Sim", "Não"])
        if adicionar_mais_escolha == "Não":
            break

    for segmento in segmentos:
        inicio = segmento["horario_inicio"]
        fim = segmento["horario_fim"]
        caminho_saida = segmento["nome_arquivo_saida"]
        imprimir_com_cor(f"ffmpeg.exe -i {video_url} -ss {inicio} -to {fim} -c copy \"{caminho_saida}\"\n", 'amarelo')
        comando = f"ffmpeg.exe -i {video_url} -ss {inicio} -to {fim} -c copy \"{caminho_saida}\""
        imprimir_com_cor(f"Baixando o segmento de {inicio} a {fim} para \"{caminho_saida}\"...\n", 'amarelo')
        subprocess.run(comando, shell=True)
        imprimir_com_cor(f"Download do segmento concluído: {caminho_saida}\n", 'verde')

input("Pressione enter para finalizar...")
