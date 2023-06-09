import os
import zipfile
pasta_atual = os.path.dirname(os.path.realpath(__file__))
nome = input("Nome do Manga: ").title()
quantidade = int(input("Quantos volumes serão: "))
volume = int(input("Qual volume inicial? "))
for v in range(volume, quantidade+1):
    if (v < 10):
        v = f'0{v}'
    fantasy_zip = zipfile.ZipFile(f'{pasta_atual}\\{nome} Volume {v}.zip', 'w')
    cap_inicial = int(input("Vai do capitulo: "))
    cap_final = int(input("Até o capitulo: "))
    for cap in range(cap_inicial, cap_final+1):
        for folder, subfolders, files in os.walk(pasta_atual):
            if folder == f'{pasta_atual}\capitulo #{cap} - {nome}':
                for file in files:
                    fantasy_zip.write(os.path.join(folder, file), os.path.relpath(
                        os.path.join(folder, file), pasta_atual), compress_type=zipfile.ZIP_DEFLATED)
                print("Compactado com sucesso")
fantasy_zip.close()
