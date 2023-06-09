import os
import zipfile
#pasta_atual = os.path.abspath(os.path.realpath(__file__)) #Retornou D:\Python\nomearquivo
#pasta_atual = os.path.dirname(os.path.realpath(__file__)) #Retornou D:\Python
#pasta_atual = os.path.samestat(s1, s2)(os.path.realpath(__file__))
pasta_atual = os.path.abspath(os.getcwd())
print(pasta_atual)

