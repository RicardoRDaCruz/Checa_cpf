Aplicação simples de Django para testar se CPFs envados como argumento da URL estão em uma Blacklist presente em um arquivo .txt externo.
O arquivo blacklist.txt está na mesma pasta do projeto (nível do manage.py). CPFs presentes na BLcklist retornam 'BLOCK', senão retornam 'FREE', na forma de JSON. CPFs em formato inválido retornam 'INVALID'
