from django.shortcuts import render
import re 
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.

def index(request):
    return JsonResponse({'message':'RUNNING'}) #retorno simples para url sem argumentos

def checa_cpf(request, value):
    padrao = re.compile(r"^[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}$") #Padrão para cconferir se o CPF é válido
    result = re.match(padrao, value)
    if str(result) == 'None':
        return JsonResponse({'message':'INVALID'})

    f = open('../blacklist.txt', 'r') #Abertura do documento de blacklist.txt, que deve estar na pasta um nível acima do projeto
    file_content = f.read()
    lista_cpf = []
    cpf=''
    for i in file_content:         # Loop para ler cada cpf do .txt e adicionálos à lista de cpfs    
        if i != '\n':
            cpf+=i
        else:                       
            lista_cpf.append(cpf)
            cpf=''
    
    for cpf in lista_cpf:           # Conferir se o cpf está na blacklist e retornar a resposta
        if value==cpf:
            return JsonResponse({'message':'BLOCK'})
        else:
            return JsonResponse({'message':'FREE'})
