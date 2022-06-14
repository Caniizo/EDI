arquivo = input("Copie todas as informações do arquivo: ")
posArq  = list(arquivo)

regCab = []
print (posArq[0:3])

if arquivo[0:3] == ("000"):
    print ("Arquivo com cabeçalho valido")
    regCab.append(arquivo[0:321])
    print (regCab)
    print (regCab[0][3:38])
    del (posArq[0:321])
    arquivo = "".join(posArq)
    print (arquivo)

