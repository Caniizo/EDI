from asyncore import write
from datetime import datetime

now = datetime.now()

anoGer = datetime.now().date().year # Ano de Geração do Arquivo
anoGer = str(anoGer) # Converte para String

mesGer = datetime.now().date().month # Mes de Geração do Arquivo
if mesGer != (10,11,12): # Valida se o mes é menor que 10 e coloca um 0 na frente
    mesGer = str(mesGer)
    mesGer = ("0" + mesGer)
    print ("cai no IF")
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

cnpjTBL = ("0")

#Registro 522
flEmissao = input ("Digite a Sigla da Filial de Emissao: ")
if flEmissao == ("81"):
    cnpjTBL = ("04503660000146")  

numCTE = input ("Informe o numero do CTe/RPS: ")
numCTE = numCTE.zfill(9)                                                                            

emiCTE = input ("Informe a data de emissão do CTE: ") 
cnpjRemetente = input ("Informe o CNPJ do Remetente: ") 
cnpjDestinatario = input ("Informe o CNPJ do Destinatario: ") # Copiado para a Janela

# Informações passadas pela 3M
manifesto = input ("Informe o numero do Manifesto: ")
serMin = input ("Informe a série da Minuta: ")

numMin = input ("Informe o numero da Minuta: ")
numMin = numMin.zfill(5) # Copiado para a Janela

emiMin = input ("Informe a data de emissão da minuta: ")

tpFrete = input ("Informe o tipo de Frete [Normal ou Complementar]: ")
tpFrete = tpFrete.upper()
tpFrete = tpFrete[0]

# Registro 523 - Valores totais do CTe
qntNF = input ("Digite o numero de NFs no CTe: ")
qntNF = int(qntNF)
conNF = 0 # Contador no Validador das NFs
nuNF = []
emiNF = []
dtTmp = False
valorNF = []
totValNF = 0
qntVol = []
totVol = 0
inpTmp = ("Jorge")

while conNF < qntNF: # Validador das NFs
    if conNF == 0:
        print ("Nenhuma nota adicionada...")
    elif conNF != 0:
        print ("NFs Adicionadas {nfs}".format(nfs=nuNF))
    NF = input ("Digite o numero da NF: ")
    NF = NF.zfill(9)
    nuNF.append(NF)
    if dtTmp == False:
        dtEmiNF = input("Digite a data de emissão da NF: ")
        emiNF.append(dtEmiNF)
        if inpTmp != ("N"):
            inpTmp = input("Todas NFs possuem a mesma data de emissão? ")
            inpTmp = inpTmp.upper()
            inpTmp = inpTmp[0]
            if inpTmp == "S":
                dtTmp = True
    elif dtTmp == True:
        emiNF.append(dtEmiNF)
   
    y = input("Digite o valor da NF {nuNF}: ".format(nuNF=nuNF[conNF])) # Pega o valor da NF e ja realiza a soma no total para o registro 523
    y = int(y)
    totValNF = y + totValNF
    y = str(y) 
    y = y.zfill(15)
    valorNF.append(y)


    y = input("Digite a quantidade de volumes da NF {nuNF}: ".format(nuNF=nuNF[conNF])) # Pega o valor de volumes da NF e ja realiza a soma no total para o registro 523
    y = int(y)
    totVol = y + totVol # Valor informado sendo adicionado ao total
    y = str(y) 
    y = y.zfill(6) # Convertendo para o minimo de 6 caracteres no arquivo
    qntVol.append(y) # Adicionado o valor para a NF
    conNF += 1 # Subindo o contador para a proxima NF
    
    
# pesoNF = input ("Digite o peso da NF") Soma simples com todos pesos
# cubagem = inpút ("Digite a cubagem da NF") Soma simples com todas cubagens
# valorNF = input ("Digite o valor da NF") 
# valorAdVal = input ("Digite o valor do Ad Valorem")
# valorSeccat = input ("Digite o valor do Sec/Cat")
# valorGris = input ("Digite o valor do Gris")
# valorTotalFrete = input ("Digite o valor Total do Frete")
# valorFrete = input ("Digite o valor do Frete")
# CFOP = input ("Digite o CFOP da NF")
# chaveAcesso = input ("Digite a chave de acesso da NF")

x = 0

with open("C:/EDI/Arquivo.txt", "w") as EDI:
    EDI.write("000TRANSPORTES BERTOLINI LTDA         3M MANAUS IND.DE PROD.QUIMICOS LTDA{dd}{mm}{yy}{hh}{m}CON{dd}{mm}{hh}{m}1".format(dd=diaGer,mm=mesGer,yy=anoGer,hh=hrGer,m=minGer))
    EDI.write("\n520CONHE{dd}{mm}{hh}{m}1".format(dd=diaGer,mm=mesGer,hh=hrGer,m=minGer))
    EDI.write("\n521{cnpjT}TRANSPORTES BERTOLINI LTDA".format(cnpjT=cnpjTBL))
    EDI.write("\n522{flEmissao}        UNI   {numCTE}   {emiCTE}F{cnpjTBL}{cnpjRemetente}00000000000000{cnpjDestinatario}{cnpjDestinatario}0000          {manifesto}                                                                                                                                                                          {serMin}  {numMin}       {emiMin}                 {tpFrete}1IN          NAMAMAM                                                                                                                        ".format(flEmissao=flEmissao,numCTE=numCTE,emiCTE=emiCTE,cnpjTBL=cnpjTBL,cnpjRemetente=cnpjRemetente,cnpjDestinatario=cnpjDestinatario,manifesto=manifesto,serMin=serMin,numMin=numMin,emiMin=emiMin,tpFrete=tpFrete))
    while x < conNF:
        EDI.write("\n524{cnpjRemetente}{nf}1  {emiNF}{valorNF}{qntVol}".format(cnpjRemetente=cnpjRemetente,nf=nuNF[x],emiNF=emiNF[x],valorNF=valorNF[x],qntVol=qntVol[x]))
        x += 1


