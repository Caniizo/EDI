from asyncio.windows_events import NULL


arquivo = []
print ("Copie todas as informações do arquivo: ")
while True:
    regArq = input()
    if regArq:
        arquivo.append(regArq)
    else:
        break

x = -1

class Agrupamento(object):
    def __init__(self, nomeDestin, nfs):
        self.nomeDestin = nomeDestin
        self.nfs = nfs


regCab = [] #000
regDoc = [] #500 
regEmb = [] #501
regEntrega = [] #502
regDest = [] #503
regLocEntr = [] #504
regNF = [] #505
regVlrNF = [] #506
regCalcFrete = [] #507
regIdenCarga = [] #508
regRedesp = [] #509
regItemNF = [] #511
regPagador = [] #513
regDadosRedesp = [] #514
regRespFrete = [] #515
regTotalArqv = [] #519
agrupamento = []
contaAgrup = []
agrupaNFS = []
agrupDest = []

while True:
    if arquivo[0][0:3] == ("000"):
        print ("Arquivo com cabeçalho valido")
        regCab.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("500"):
        print ("Arquivo com cabeçalho de documento valido")
        regDoc.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("501"):
        print ("Registro da Embarcadora validado")
        regEmb.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("502"):
        print ("Registro de Entrega Validado")
        regEntrega.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("503"):
        print ("Registro do Destinatario validado")
        regDest.append(arquivo[0][0:321])
        agrupDest.append(arquivo[0][3:53])
        arquivo.pop(0)
        x += 1
        agrupamento.append(x)
        agrupaNFS.clear()
        while arquivo[0][0:3] != ("503"):
            if arquivo[0][0:3] == ("504"):
                print ("Registro do Local de Entrega validado")
                regLocEntr.append(arquivo[0][0:321])
                arquivo.pop(0)        
            elif arquivo[0][0:3] == ("505"):
                print ("Registro da Nota Fiscal validado")
                regNF.append(arquivo[0][0:321])
                agrupaNFS.append(arquivo[0][6:15])
                print (x)
                if agrupamento[x].nomeDestin is not None:
                    print (agrupamento[x].nomeDestin)
                    print (agrupamento[x].nfs)
                agrupamento[x] = Agrupamento(nomeDestin=agrupDest, nfs=agrupaNFS)
                print (agrupamento[x].nomeDestin)
                print (agrupamento[x].nfs)
                print ("Codigo acima rodou após pegar o valor")
                agrupDest.clear() 
                arquivo.pop(0)
                print (agrupamento[x].nomeDestin)
                print (agrupamento[x].nfs)
                print ("Codigo acima rodou após limpar o agrupDest")
            elif arquivo[0][0:3] == ("506"):
                print ("Registro dos Valores das NFs validado")
                regVlrNF.append(arquivo[0][0:321])
                arquivo.pop(0)            
            elif arquivo[0][0:3] == ("507"):
                print ("Registro do Calculo de Frete validado")
                regCalcFrete.append(arquivo[0][0:321])
                arquivo.pop(0)
            elif arquivo[0][0:3] == ("508"):
                print ("Registro da Identificação da Carga validado")
                regIdenCarga.append(arquivo[0][0:321])
                arquivo.pop(0)
            elif arquivo[0][0:3] == ("509"):
                print ("Registro do Redespacho validado")
                regRedesp.append(arquivo[0][0:321])
                arquivo.pop(0)
            elif arquivo[0][0:3] == ("511"):
                print ("Registro do Item da NF validado")
                regItemNF.append(arquivo[0][0:321])
                arquivo.pop(0)
            else:
                break    
    elif arquivo[0][0:3] == ("513"):
        print ("Registro do Pagador validado")
        regPagador.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("514"):
        print ("Registro dos Dados do Redespacho validado")
        regDadosRedesp.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("515"):
        print ("Registro do Responsavel pelo Frete validado")
        regRespFrete.append(arquivo[0][0:321])
        arquivo.pop(0)
    elif arquivo[0][0:3] == ("519"):
        print ("Registro de Valores Totais validado")
        regTotalArqv.append(arquivo[0][0:321])
        arquivo.pop(0)
        break                                                       
    else:
        break

while True:
    print ("Que informação precisa?\n Informações Gerais (IG)")
    inpInfo = input()
    inpInfo = inpInfo.upper()
    print (agrupamento[0].nomeDestin)
    print (agrupamento[0].nfs)
    print (agrupamento[1].nomeDestin)
    print (agrupamento[1].nfs)
    print (len(agrupamento))
    if inpInfo == ("IG"):
        while x < len(regNF):
            print ("NF " + regNF[x][6:15])
            x += 1



