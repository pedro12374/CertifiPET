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
k=k+''''no dia ''' + n_data[2] + ''', realizado pelo Programa de Educa��o Tutorial em F�sica (PET-F�SICA) da Universidade Estadual de Maring�, com carga hor�ria total de '''
k=k+n_data[3]+''' ('''+n_data[4]+''').

'''
today = datetime.date.today()
k=k+'''Maring�-PR,''' + today.strftime('%d de %B de %Y').lower()
print k

