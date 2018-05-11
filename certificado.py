#coding: utf-8
import os,datetime,locale
from PIL import ImageFont
from shutil import copy2
locale.setlocale(locale.LC_ALL, '')

data = open('nomes.txt','r')
n_data = data.readlines()
n_data = map(lambda s: s.strip(),n_data)



if os.access(n_data[1],os.F_OK)== False:
    os.mkdir(n_data[1])

copy2("PET.png", str(n_data[1]))
copy2("Cabecalho.png", str(n_data[1]))
os.chdir(n_data[1])

tam=len(n_data)
for num in range(5,tam-1):
    cert = '''
    \documentclass[12pt,a4paper]{memoir}
    \usepackage{lipsum}
    \usepackage{graphicx}
    \usepackage{background}
    \usepackage[utf8]{inputenc}
    \usepackage[brazilian]{babel}
    \usepackage{lmodern}
    \setlength{\parindent}{0pt}
    \\backgroundsetup{contents={\includegraphics[scale=0.4]{PET.png}},angle=0,scale=3.3}

    \usepackage{wallpaper}
    \usepackage[tmargin=8.7cm,rmargin=3cm,lmargin=3cm,bmargin=1.25cm]{geometry}
    \\addtolength{\wpXoffset}{-3.2cm}%Maor o numero, mais para a direita
    \\addtolength{\wpYoffset}{10cm}%Maior o numero, mais para cima
    \pagenumbering{gobble}

    \\begin{document}
    \CenterWallPaper{1.15}{Cabecalho.png}


    \\begin{center}
        \HUGE{CERTIFICADO}\\\[50pt]
    \end{center}
    \\noindent
    '''

    cert = cert+'''
    {\\fontsize{19pt}{24pt} \selectfont Certificamos que ''' + n_data[num]
    cert = cert+''' participou do '''+n_data[0]+''': "'''+n_data[1]+'''" no dia '''+n_data[2]+''', realizado pelo Programa de Educação Tutorial em Física (PET-FÍSICA) da Universidade Estadual de Maringá, com carga horária total de '''+n_data[3]+''' '''+n_data[4]+''' HORAS. }\\\[30pt]'''
    today = datetime.date.today()
    dia = today.strftime('%d de %B de %Y').lower()


    cert = cert+'''
    \\begin{center}
    {\\fontsize{19pt}{24pt} \selectfont Maringá-PR, '''+dia+'''.}\\\\[220pt]
    \end{center}

    \\begin{center}
    
    $\\rule{10cm}{0.15mm}$\\\\





    Tutor Prof. Dr. Marcos Cesar Danhoni Neves

    
    
    \end{center}
    \end{document}
    '''

    nome = n_data[num].replace(' ','_')
    print nome
    f = open(str(nome)+ ".tex","w")
    f.write(cert)
    f.close()
    cert=""

    temp=os.getcwd()

    os.system('pdflatex '+nome+'.tex')
    os.system('pdflatex '+nome+'.tex')
    os.system('pdflatex '+nome+'.tex')
    os.remove(os.getcwd()+'/'+nome+'.aux')
    os.remove(os.getcwd()+'/'+nome+'.log')
    os.remove(os.getcwd()+'/'+nome+'.tex')
