# CertifiPET
Programa em python feito para geração de Certificados em LaTeX

# Instalação
Só é nescessario clonar o arquivo certificados.py e ter Python 2.7 instalado em uma maquina Linux

# Utilização

Para utilizar este programa é necessário um arquivo de texto chamado 'nomes.txt', e dentro dele em ordem:

- Tipo de Atividade(Ex: Seminário, Apresentação, Palestra)
- Nome da Atividade
- Data em que ocorreu a Atividade
- Quantidade de horas concedidas em formato numérico(Ex: 3)
- Quantidade de horas concedidas por extenso dentro de um parêntese(Ex: (Três) )
- Nomes dos participantes, um por linha
- Na última linha, o nome do responsável pela atividade

Também deve ser criada uma pasta com o nome idêntico ao preenchido no *Nome da Atividade* e dentro desta pasta colocado os arquivos de cabeçalho e marca d’água

# Avisos

**No caso deste programa, o nome do Tutor atual do grupo está presente pois ele tambem é responsavel, e isso deve ser alterado no arquivo certificado.py na linha 65**

**Nas linhas 25 e 34 respectivamentes estão os nomes dos arquivos de imagem que compõem a marca d'água e o cabeçalho do certificado. Estes dois arquivos devem ser adaptados a sua situação específica. *Neste caso, a marca d'água está com o nome de PET.png e o cabeçalho de cabecalho.png***


