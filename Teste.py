import os,datetime#,locale
import os
import shutil

direc = os.getcwd()
#locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

print direc
data = open('nomes.txt','r')

n_data = data.readlines()
n_data = map(lambda s: s.strip(),n_data)


if os.access(n_data[1],os.F_OK)== False:
    os.mkdir(n_data[1])
os.chdir(n_data[1])
#sub = open('Teta.txt','r')
#print sub.readlines()
for i in range(5):
    os.system("touch "+str(i)+".txt")


'''
y=len(n_data)
print y
for num in range(5,y-1):
    print n_data[num]


from PIL import ImageFont
font = ImageFont.truetype('Comic Sans MS.ttf', 12)
size = font.getsize('Hello world')
print(size)
'''
