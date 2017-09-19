#!/usr/bin/python3
import pandas as pd
import os
import requests

def log(error):
  f = open('error.log','a')
  f.write(error)


def latex_sanitize(text):
  return text.replace("%","\\%").replace("$","\\$").replace("#","\\#").replace("_","\\_").replace("&","\\&").replace("{","\\{").replace("}","\\}")

############################################################################################################
  
def slugify(value):
  import string
  valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
  return ''.join(c for c in value if c in valid_chars)

def formatCPF(cpfn):
  cpft = str(cpfn)[:-8]+"."+str(cpfn)[-8:-5]+"."+str(cpfn)[-5:-2]+"-"+str(cpfn)[-2:]
  while (len(cpft) < 14):
    cpft = "0"+cpft
  return cpft
  

############################################################################################################

def trab_OK(trab):
  return not (pd.isnull(trab['Nome']) or pd.isnull(trab['Autores']) or pd.isnull(trab['Orientador']) or pd.isnull(trab['Cargo']) or pd.isnull(trab['PET']) or pd.isnull(trab['Universidade']) or pd.isnull(trab['Situação']))

############################################################################################################

def gen_carta(trab):
  import os
  import datetime
  import locale
  
  locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
  
  carta = """\\documentclass[a4paper,landscape,14px]{article}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage{graphicx,color}
\\usepackage[utf8]{inputenc}
\\usepackage[portuges]{babel}
\\usepackage{anyfontsize}
\\usepackage{eso-pic,graphicx}
\\usepackage[top=7cm, bottom=0cm, left=3cm, right=3cm]{geometry}
\\usepackage{calligra}
\\usepackage{float}

\\begin{document}

\\begin{center}
\\LARGE\\textbf{DECLARAÇÃO DE PARTICIPAÇÃO}\\\\[1cm]
\\end{center}

\\Large """
  carta = carta+"Declaramos que "+latex_sanitize(trab['Nome'])+", CPF nº "+latex_sanitize(formatCPF(trab['CPF']))+", "+latex_sanitize(trab['Categoria'])+" do PET "+latex_sanitize(trab['PET'])+" da "+latex_sanitize(trab['Instituicao'])+" participou do XXII Encontro Nacional dos Grupos PET – XXII ENAPET, no período "+latex_sanitize(trab['Periodo'])+" de julho de 2017, em Brasília – DF."
  carta = carta+"""\\\\
\\begin{flushright}
Brasília, """
  today = datetime.date.today()
  carta = carta+today.strftime('%d de %B de %Y').lower()
  carta = carta+"""
\\end{flushright}
\\AddToShipoutPictureBG*{\\includegraphics[width=\\paperwidth,height=\\paperheight]{fundo.pdf}}
\\end{document}"""

  tex = open("tmp.tex",'w')
  tex.write(carta)
  tex.close()
  
  name = slugify(trab['Nome'])
  texlog = os.system("pdflatex --file-line-error-style -output-directory=./emitidas -jobname=\""+name+"\" tmp.tex >> latex.log")
  return "emitidas/"+name+".pdf"

############################################################################################################

def send_mail(to,subject,body,attachment):
  return requests.post(
    "https://api.mailgun.net/v3/enapetbsb.com/messages",
    auth=("api", "chave da api do mailgun"),
    files=[("attachment", open(attachment,'rb'))],
    data={"from": "Amã do XXII ENAPET <ama@enapetbsb.com>",
      "to": to,
      "subject": subject,
      "html": body})

data = pd.read_excel('lista.xlsx', 'Para_emitir', index_col=None, na_values=['NA'])

for i,declaracao in data.iterrows():
  print("#"+str(i+2))
  print("  Gerando declaração: "+declaracao['Nome'])
  
  filename = gen_carta(declaracao)
  print("  Declaração gerada: "+filename)
  
  assunto = "[XXII ENAPET] Declaração de participação"
  texto = """Olá,<br><br>
Segue em anexo a sua declaração de participação.<br><br>
Juliano Genari"""

  print("  Eviando e-mail: "+declaracao['E-mail'])
  r = send_mail(declaracao['E-mail'],assunto,texto,filename)
  
  if r.status_code != requests.codes.ok:
    print("    ERRO NO ENVIO DO E-MAIL!")
  else:
    print("  E-mail enviado!")
