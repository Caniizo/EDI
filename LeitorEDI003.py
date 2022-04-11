regDestinatario = []
regNotaFiscal = []
regInfo = False
info = False

while regInfo == False:
    inputReg = input("Cole UMA linha de registro por vez: ")
    if inputReg[0:3] == ("503"):
        regDestinatario.append(inputReg)
        print ("Registro de destinatario validado")
    elif inputReg[0:3] == ("505"):
        regNotaFiscal.append(inputReg)
        print ("Registro de nota fiscal validado")
    else:
        print ("Registro invalido, verifique")
    quitReg = input("Deseja adicionar um novo registro? ")
    if quitReg == ("s"):
        pass
    elif quitReg == ("n"):
        break
    else:
        print ("Opção invalida")

while info == False:
    inpInfo = input("Digite o que precisa saber: CNPJ do Remetente (CR), Nota Fiscal (NF) ")


