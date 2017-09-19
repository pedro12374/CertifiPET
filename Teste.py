import os,datetime#,locale
#locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")


data = open('nomes.txt','r')

n_data = data.readlines()
n_data = map(lambda s: s.strip(),n_data)

k = '''
Certificamos que '''

k = k + n_data[5]

k = k+''' participou do '''
k=k+ n_data[0]+''': "'''+n_data[1]+'''"'''
k=k+''''no dia ''' + n_data[2] + ''', realizado pelo Programa de Educação Tutorial em Física (PET-FÍSICA) da Universidade Estadual de Maringá, com carga horária total de '''
k=k+n_data[3]+''' ('''+n_data[4]+''').

'''
today = datetime.date.today()
k=k+'''Maringá-PR,''' + today.strftime('%d de %B de %Y').lower()
print k

