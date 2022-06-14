from glob import glob
from tkinter import *
from asyncore import write
from datetime import datetime

now = datetime.now()

anoGer = datetime.now().date().year # Ano de Geração do Arquivo
anoGer = str(anoGer) # Converte para String

mesGer = datetime.now().date().month # Mes de Geração do Arquivo
if mesGer != (10,11,12): # Valida se o mes é menor que 10 e coloca um 0 na frente
    mesGer = str(mesGer)
    mesGer = ("0" + mesGer)
mesGer = str(mesGer) # Converte para String


diaGer = datetime.now().date().day # Dia de Geração do Arquivo
if diaGer == (1,2,3,4,5,6,7,8,9): # Valida se o dia é menor que 10 e coloca um 0 na frente
    mesGer = str(diaGer)
    mesGer = ("0" + diaGer)
diaGer = str(diaGer) # Converte para String


hrGer = datetime.now().hour # Hora de Geração do Arquivo
hrGer = str(hrGer) # Converte para String

minGer = datetime.now().minute # Minuto de Geração do Arquivo
minGer = str(minGer) # Converte para String

cnpjTBL = ("")
flEmissao = ()
numCTE = ()
emiCTE = ()
cnpjRemetente = ()
cnpjDestinatario = ()
manifesto = ()
serMin = ()
numMin = ()
emiMin = ()
tpFrete = ()

nuNF = []
dataNF = []
valorNF = []
pesoNF = []
cfop = []
chaveNF = []
qntvolNF = []

global totVol
totVol = 0
totPeso = 0


global x 
x = 0
global y
y = 0

root = Tk()
root.title("Gerador de Arquivos 3M")
root.iconbitmap("C:/DEV/StudioCode/Gerador.ico")
root.geometry("700x350")

def clique():
    #bot_Alter["state"] = NORMAL
    #bot_Alter["text"] = "Alterar Informações"
    global y
    bot_Conf["text"] = "Regerar Arquivo"
    flEmissao = but_flEmissao.get()
    if flEmissao == ("81"):
        cnpjTBL = ("04503660000146")
    numCTE = but_numCTE.get()
    numCTE = numCTE.zfill(9)
    emiCTE = but_emiCTE.get()
    cnpjRemetente = but_cnpjRemetente.get()
    cnpjDestinatario = but_cnpjDestinatario.get()
    manifesto = but_manifesto.get()
    serMin = but_serMin.get()
    numMin = but_numMin.get()
    numMin = numMin.zfill(5)
    emiMin = but_emiMin.get()
    tpFrete = but_tpFrete.get()
    tpFrete = tpFrete.upper()
    tpFrete = tpFrete[0]
    totVol = str(totVol)
    totVol = totVol.zfill(6)

    print (cfop)
    print (chaveNF)


    with open("C:/EDI/ArquivoTesteGUI.txt", "w") as EDI:
        EDI.write("000TRANSPORTES BERTOLINI LTDA         3M MANAUS IND.DE PROD.QUIMICOS LTDA{dd}{mm}{yy}{hh}{m}CON{dd}{mm}{hh}{m}1                                                                                                                                                                                                                                                                                                                                                                                                      ".format(dd=diaGer,mm=mesGer,yy=anoGer,hh=hrGer,m=minGer))
        EDI.write("\n520CONHE{dd}{mm}{hh}{m}1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ".format(dd=diaGer,mm=mesGer,hh=hrGer,m=minGer))
        EDI.write("\n521{cnpjT}TRANSPORTES BERTOLINI LTDA                                                                                                                                                                                                                                                                                                                                                                                                                                                          ".format(cnpjT=cnpjTBL))
        EDI.write("\n522{flEmissao}        UNI   {numCTE}   {emiCTE}F{cnpjTBL}{cnpjRemetente}00000000000000{cnpjDestinatario}{cnpjDestinatario}0000          {manifesto}                                                                                                                                                                          {serMin}  {numMin}       {emiMin}                 {tpFrete}1IN          NAMAMAM                                                                                                                        ".format(flEmissao=flEmissao,numCTE=numCTE,emiCTE=emiCTE,cnpjTBL=cnpjTBL,cnpjRemetente=cnpjRemetente,cnpjDestinatario=cnpjDestinatario,manifesto=manifesto,serMin=serMin,numMin=numMin,emiMin=emiMin,tpFrete=tpFrete))
        EDI.write("\n523{totVol}".format(totVol=totVol))
        while y < len(nuNF):
            EDI.write("\n524{cnpjRemetente}{nuNF}1  {dataNF}{valorNF}{qntvolNF}00{pesoNF}00000000000000000000                                                                                                     1 {cfop}            {chaveNF}                                                                                                                                                                                                                                         ".format(cnpjRemetente=cnpjRemetente,nuNF=nuNF[y],dataNF=dataNF[y],valorNF=valorNF[y],qntvolNF=qntvolNF[y],pesoNF=pesoNF[y],cfop=cfop[y],chaveNF=chaveNF[y]))
            y += 1


def clique_NF(): # Função ao clicar no botão "NFS"

    # Limpa a Tela Inicial
    bot_NF.grid_forget()
    bot_Conf.grid_forget()
    texto_1.grid_forget()
    texto_2.grid_forget()
    texto_3.grid_forget()
    texto_4.grid_forget()
    texto_5.grid_forget()
    texto_6.grid_forget()
    texto_7.grid_forget()
    texto_8.grid_forget()
    texto_9.grid_forget()
    texto_10.grid_forget()
    but_flEmissao.grid_forget()
    but_numCTE.grid_forget()
    but_emiCTE.grid_forget()
    but_cnpjRemetente.grid_forget()
    but_cnpjDestinatario.grid_forget()
    but_manifesto.grid_forget()
    but_serMin.grid_forget()
    but_numMin.grid_forget()
    but_emiMin.grid_forget()
    but_tpFrete.grid_forget()
    
    # Frame das NFs
    global frame_infoNFS 
    frame_infoNFS = LabelFrame(root, text="Informações da NF")
    frame_infoNFS.grid(row=0, column=0)
    
    # Textos e Posicionamentos das NFs
    global textoNF_1
    textoNF_1 = Label(frame_infoNFS, text="Numero da NF")
    textoNF_1.grid(row=0, column=0)
    global textoNF_2
    textoNF_2 = Label(frame_infoNFS, text="Data de Emissão da NF")
    textoNF_2.grid(row=1, column=0)
    global textoNF_3
    textoNF_3 = Label(frame_infoNFS, text="Valor da NF")
    textoNF_3.grid(row=2, column=0)
    global textoNF_4
    textoNF_4 = Label(frame_infoNFS, text="Volumes da NF")
    textoNF_4.grid(row=3, column=0)
    global textoNF_5
    textoNF_5 = Label(frame_infoNFS, text="Peso da NF")
    textoNF_5.grid(row=4, column=0)
    global textoNF_6
    textoNF_6 = Label(frame_infoNFS, text="CFOP da NF")
    textoNF_6.grid(row=5, column=0)
    global textoNF_7
    textoNF_7 = Label(frame_infoNFS, text="Chave de Acesso da NF")
    textoNF_7.grid(row=6, column=0)

    
    # Entrada e Posicionamentos das NFs
    global bot_nuNF
    bot_nuNF = Entry(frame_infoNFS, width=15)
    bot_nuNF.grid(row=0, column=1)
    global bot_dataNF
    bot_dataNF = Entry(frame_infoNFS, width=15)
    bot_dataNF.grid(row=1, column=1)
    global bot_valorNF
    bot_valorNF = Entry(frame_infoNFS, width=15)
    bot_valorNF.grid(row=2, column=1)
    global bot_qntvolNF
    bot_qntvolNF = Entry(frame_infoNFS, width=15)
    bot_qntvolNF.grid(row=3, column=1)
    global bot_pesoNF
    bot_pesoNF = Entry(frame_infoNFS, width=15)
    bot_pesoNF.grid(row=4, column=1)
    global bot_cfopNF
    bot_cfopNF = Entry(frame_infoNFS, width=15)
    bot_cfopNF.grid(row=5, column=1)
    global bot_chaveNF
    bot_chaveNF = Entry(frame_infoNFS, width=30)
    bot_chaveNF.grid(row=6, column=1)


    global bot_confNF
    bot_confNF = Button(frame_infoNFS, text="Adicionar NF", command=clique_confirmaNF)
    bot_confNF.grid(row=2, column=3)


    global status
    status = Label(root, text=str(len(nuNF)) + " NFs Adicionada ")
    status.grid(row=4, column=3)

    #global bot_lisNF
    #bot_lisNF = Button(root, text="Lista de NFs", command=clique_listaNF)
    #bot_lisNF.grid(row=2, column=4)

    global  bot_voltar
    bot_voltar = Button(root, text="Voltar", command=clique_retorno)
    bot_voltar.grid(row=4, column=2)

def clique_confirmaNF(): # Função ao clicar em "Adicionar NF" dentro da tela de NFS
    global bot_nuNF
    global status
    global bot_dataNF
    global bot_valorNF
    global bot_qntvolNF
    global bot_pesoNF
    global bot_cfopNF
    global bot_chaveNF
    global totVol
    global totPeso
    global notas
    global x


    if x == 0:
        notas = LabelFrame(root, text="Notas")
        notas.grid(row=0, column=5)
    status.grid_forget()

    bot_nuNF = bot_nuNF.get()
    bot_nuNF = bot_nuNF.zfill(9)
    nuNF.append(bot_nuNF)

    dataNF.append(bot_dataNF.get())
    tmpNF = bot_dataNF.get()

    bot_valorNF = bot_valorNF.get()
    bot_valorNF = bot_valorNF.zfill(15)
    valorNF.append(bot_valorNF)

    bot_qntvolNF = bot_qntvolNF.get()
    bot_qntvolNF = int(bot_qntvolNF)
    totVol = bot_qntvolNF + totVol
    bot_qntvolNF = str(bot_qntvolNF)
    bot_qntvolNF = bot_qntvolNF.zfill(6)
    qntvolNF.append(bot_qntvolNF)

    bot_pesoNF = bot_pesoNF.get()
    bot_pesoNF = float(bot_pesoNF)
    totPeso = bot_pesoNF + totPeso
    bot_pesoNF = str(bot_pesoNF)
    bot_pesoNF = bot_pesoNF.zfill(9)
    pesoNF.append(bot_pesoNF)

    cfop.append(bot_cfopNF.get())
    chaveNF.append(bot_chaveNF.get())


    bot_nuNF = Entry(frame_infoNFS, width=15)
    bot_nuNF.grid(row=0, column=1)
    bot_dataNF = Entry(frame_infoNFS, width=15)
    bot_dataNF.insert(0, tmpNF)
    bot_dataNF.grid(row=1, column=1)
    bot_valorNF = Entry(frame_infoNFS, width=15)
    bot_valorNF.grid(row=2, column=1)
    bot_qntvolNF = Entry(frame_infoNFS, width=15)
    bot_qntvolNF.grid(row=3, column=1)
    bot_pesoNF = Entry(frame_infoNFS, width=15)
    bot_pesoNF.grid(row=4, column=1)
    bot_cfopNF = Entry(frame_infoNFS, width=15)
    bot_cfopNF.grid(row=5, column=1)
    bot_chaveNF = Entry(frame_infoNFS, width=30)
    bot_chaveNF.grid(row=6, column=1)



    status = Label(root, text=str(len(nuNF)) + " NFs Adicionada ")
    status.grid(row=3, column=3)
    
    print (cfop)
    print (chaveNF)


    while x < len(nuNF):
        
        texto_liNF = Label(notas, text="NF")
        texto_liNF.grid(row=0, column=0)
        texto_liDt = Label(notas, text="Data de Emissão")
        texto_liDt.grid(row=0, column=1)

        nota = Label(notas, text=nuNF[x])
        nota.grid(row=x + 1, column=0)
        x += 1
    

def clique_retorno(): # Função ao clicar em "Voltar" dentro da tela de NFS
    bot_voltar.grid_forget()
    frame_infoNFS.grid_forget()
    if x != 0:
        notas.grid_forget()
    texto_1.grid(row=0, column=0)
    texto_2.grid(row=1, column=0)
    texto_3.grid(row=2, column=0)
    texto_4.grid(row=3, column=0)
    texto_5.grid(row=4, column=0)
    texto_6.grid(row=5, column=0)
    texto_7.grid(row=6, column=0)
    texto_8.grid(row=7, column=0)
    texto_9.grid(row=8, column=0)
    texto_10.grid(row=9, column=0)
    but_flEmissao.grid(row=0, column=1)
    but_numCTE.grid(row=1, column=1)
    but_emiCTE.grid(row=2, column=1)
    but_cnpjRemetente.grid(row=3, column=1)
    but_cnpjDestinatario.grid(row=4, column=1)
    but_manifesto.grid(row=5, column=1)
    but_serMin.grid(row=6, column=1)
    but_numMin.grid(row=7, column=1)
    but_emiMin.grid(row=8, column=1)
    but_tpFrete.grid(row=9, column=1)
    bot_NF.grid(row=2, column=3)
    bot_Conf.grid(row=1, column=3)

bot_NF = Button(root, text="NFS", command=clique_NF)
bot_NF.grid(row=2, column=3)
bot_Conf = Button(root, text="Confirmar Informações", command=clique)
bot_Conf.grid(row=1, column=3)


# Textos da Tela Inicial
texto_1 = Label(root, text="Sigla da Filial de Emissao")
texto_2 = Label(root, text="Numero do CTe/RPS")
texto_3 = Label(root, text="Data de emissão do CTE")
texto_4 = Label(root, text="CNPJ do Remetente")
texto_5 = Label(root, text="CNPJ do Destinatario")
texto_6 = Label(root, text="Manifesto")
texto_7 = Label(root, text="Série da Minuta")
texto_8 = Label(root, text="Minuta")
texto_9 = Label(root, text="Data de Emissão da Minuta")
texto_10 = Label(root, text="Tipo De Frete")

# Entradas da Tela Inicial
but_flEmissao = Entry(root, width=15)
but_numCTE = Entry(root, width=15)
but_emiCTE = Entry(root, width=15)
but_cnpjRemetente = Entry(root, width=15)
but_cnpjDestinatario = Entry(root, width=15)
but_manifesto = Entry(root, width=15)
but_serMin = Entry(root, width=15)
but_numMin = Entry(root, width=15)
but_emiMin = Entry(root, width=15)
but_tpFrete = Entry(root, width=15)

# Posicionamento dos textos
texto_1.grid(row=0, column=0)
texto_2.grid(row=1, column=0)
texto_3.grid(row=2, column=0)
texto_4.grid(row=3, column=0)
texto_5.grid(row=4, column=0)
texto_6.grid(row=5, column=0)
texto_7.grid(row=6, column=0)
texto_8.grid(row=7, column=0)
texto_9.grid(row=8, column=0)
texto_10.grid(row=9, column=0)

#Posicionamento das Entradas
but_flEmissao.grid(row=0, column=1)
but_numCTE.grid(row=1, column=1)
but_emiCTE.grid(row=2, column=1)
but_cnpjRemetente.grid(row=3, column=1)
but_cnpjDestinatario.grid(row=4, column=1)
but_manifesto.grid(row=5, column=1)
but_serMin.grid(row=6, column=1)
but_numMin.grid(row=7, column=1)
but_emiMin.grid(row=8, column=1)
but_tpFrete.grid(row=9, column=1)

root.mainloop()