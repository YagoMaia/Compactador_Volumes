import os
import zipfile

class colors: 
    nada = "\033[m"
    vermelho = '\033[1;31m'
    verde = '\033[1;32m'
    amarelo = '\033[1;33m'
    azul = '\033[1;34m'
    roxo = '\033[1;35m'
    ciano = '\033[1;36m'
    cinza = '\033[1;37m'

pasta_atual = os.path.dirname(os.path.realpath(__file__))
nome_manga = os.path.basename(pasta_atual)


volumes_e_cap = {"Volume": "", "Cap_Ini": "", "Cap_Fim": ""}

quantidade = int(input("Quantos volumes serão: "))
volume = int(input("Qual volume inicial? "))

for v in range(volume, volume + quantidade + 1):
    if (v < 10):
        v = f'0{v}'
    fantasy_zip = zipfile.ZipFile(
        f'{pasta_atual}\\{nome_manga} Volume {v}.zip', 'w')
    print(f"Capitulos do Volume {v}")
    cap_inicial = int(input("Capitulo Inicial: "))
    if (cap_inicial == -1):
        print(f"{colors.vermelho}Saída Forçada do Programa{colors.nada}")
        break
    cap_final = int(input("Capitulo Final: "))
    for cap in range(cap_inicial, cap_final+1):
        for folder, subfolders, files in os.walk(pasta_atual):
            if folder == f'{pasta_atual}\capitulo #{cap} - {nome_manga}':
                for file in files:
                    fantasy_zip.write(os.path.join(folder, file), os.path.relpath(
                        os.path.join(folder, file), pasta_atual), compress_type=zipfile.ZIP_DEFLATED)
                print(f"{colors.verde}Capitulo compactado com sucesso{colors.nada}")
print(f"{colors.azul}Programa Finalizado{colors.nada}")
fantasy_zip.close()
