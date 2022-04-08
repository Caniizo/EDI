reg = input("Cole todo o arquivo: ")

registros = {"embarcador": "501", "destinatario": "503", "nota_fiscal": "505"}

print (registros["destinatario"])

cabInt = reg[0:320]

if cabInt[0:3] == "000":
    print("Cabecalho validado")
else:
   print("Cabecalho invalido")

# posInicial = input("Informe a nota fiscal que deseja: ")
# posInicial = int(posInicial)
# posInicial = posInicial - 1
# posFinal = input("Informe a posição final do que precisa encontrar: ")
# posFinal = int(posFinal)
# posFinal = posFinal - 1
# print (reg[posInicial:posFinal])

standby = input("Deseja realizar uma nova consulta? ")

while standby == "s" or standby == "S" or standby == "Sim" or standby == "sim":
    posInicial = input("Informe a posição inicial do que precisa encontrar: ")
    posInicial = int(posInicial)
    posInicial = posInicial - 1
    posFinal = input("Informe a posição final do que precisa encontrar: ")
    posFinal = int(posFinal)
    posFinal = posFinal - 1
    print (reg[posInicial:posFinal])
    standby = input("Deseja realizar uma nova consulta? ")
