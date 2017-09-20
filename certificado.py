
import os,datetime#,locale
#locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")


data = open('nomes.txt','r')

n_data = data.readlines()
n_data = map(lambda s: s.strip(),n_data)



cert = '''
\documentclass[12pt,a4paper]{memoir}
\usepackage{lipsum}

\usepackage{graphicx}
\usepackage{background}
\usepackage[utf8]{inputenc}
\usepackage[brazilian]{babel}
\usepackage{lmodern}
\setlength{\parindent}{0pt}
\backgroundsetup{contents={\includegraphics[scale=0.4]{PET.png}},angle=0,scale=3.3}

\usepackage{wallpaper}

\usepackage[tmargin=8.7cm,rmargin=3cm,lmargin=3cm,bmargin=1.25cm]{geometry}
\addtolength{\wpXoffset}{-3.2cm}%Maor o numero, mais para a direita
\addtolength{\wpYoffset}{10cm}%Maior o numero, mais para cima







\begin{document}
\CenterWallPaper{1.15}{Cabecalho.png}


\begin{center}
    \HUGE{CERTIFICADO}\\[50pt]
\end{center}
'''
for num in range(len(n_data)-5):
    temp=num+5
    cert = cert+'''{\fontsize{19pt}{24pt} \selectfont Certificamos que ''' + n_data(k)

cert = cert+'''participou do '''+n_data[0]+''': “'''+n_data[1]+'''” no dia '''+n_data[2]+''', realizado pelo Programa de Educação Tutorial em Física (PET-FÍSICA) da Universidade Estadual de Maringá, com carga horária total de '''+n_data[3]+''' '''+n_data[4]+''' HORAS]. }\\[30pt]'''

today = datetime.date.today()
dia = today.strftime('%d de %B de %Y').lower()

cert = cert+'''
\begin{center}
{\fontsize{19pt}{24pt} \selectfont Maringá-PR, '''+dia+'''.}\\[220pt]
\end{center}
\begin{flushleft}
$\rule{6cm}{0.15mm}$\hfill$\rule{6cm}{0.15mm}$\\
\footnotesize{\hspace{40pt} '''+n_data[-1]+'''\hfill MARCOS CESAR DANHONI NEVES\\
\hspace{60pt}PET-Física\hspace{185pt} Professor Tutor}
\end{flushleft}
\end{document}
'''




for i in range(len(n_data-5):
    f = open(str(n_data[i+5])+ ".tex","w")
    f.write(cert)
    f.close()
