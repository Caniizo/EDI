from ctypes import util
from turtle import clear

class Ramais(object):
    def __init__(self, nomeRamal, numRamal, depRamal):
        self.nomeRamal = nomeRamal
        self.numRamal = numRamal
        self.depRamal = depRamal


x = 0
priVal = False
filiais = ["Manaus", "Rio Negrinho", "Bento Gonçalves", "Porto Velho", "Belem", "Boa Vista", "Aparecida de Goiania", "Macapa", "Fortaleza", "Santarem", "Guarulhos", "Itaituba", "Paragominas", "Curitiba", "Ji-Parana", "Rio Branco", "Alta Mira", "Maraba", "Cujubinzinho", "Guarai", "Contagem", "Ipojuca", "Campo Grande", "Cuiaba", "Itajai"]
codFiliais = ["1", "2", "3", "4", "5", "7", "10", "11", "12", "13", "14", "20", "21", "22", "23", "27", "29", "30", "32", "33", "35", "37", "40", "B1", "B2"]
idFiliais = ["MAO", "RNG", "BGV", "PVH", "BEL", "BVB", "GYN", "MCP", "FOR", "STM", "GRU", "ITB", "PRG", "CWB", "JPR", "RBR", "ATM", "MAB", "CBI", "GRI", "BHZ", "IPJ", "CGR", "CGB", "ITA"]
cnpjFiliais = ["04503660000146", "04503660000227", "04503660000308", "04503660000499", "04503660000570", "04503660000731", "04503660001037", "04503660001118", "04503660001207", "04503660001380", "04503660001460", "04503660002009", "04503660002190", "04503660002270", "04503660002351", "04503660002785", "04503660002947", "04503660003080", "04503660003242", "04503660003323", "04503660003595", "04503660003757", "04503660004052", "04503660004133", "04503660004214"]
codGerFil = list(zip(codFiliais, idFiliais, filiais, cnpjFiliais))
varFil = filiais, codFiliais, idFiliais, cnpjFiliais
def encontraFilial(infoCodFil, codFiliais, y, idFiliais, filiais, cnpjFiliais,filialEncontrada, varFil):  
    if infoCodFil in varFil:
        while y < 25:
            if infoCodFil == varFil[y]:
                filialEncontrada = (y)
            y += 1
    print(codFiliais[filialEncontrada], idFiliais[filialEncontrada], filiais[filialEncontrada],cnpjFiliais[filialEncontrada])

proUtiOps = ("Checar CT-e: (1)", "Consultar Cliente: (2)") 

namRam = ["Vanderlei", "Alberto", "Alex", "Cesar", "Cristian", "Darlan", "Diogo", "Gomes", "João", "Luciano", "Lucas", "Gustavo", "Juliano", "Marcos", "Roberto", "Rovilso", "Bruno", "Eduardo", "Eric", "Felipe", "Idevaldo", "Julian", "Laura", "Rizzi", "Rafael"]
nomes = ["Vanderlei", "Alberto", "Alex", "Cesar", "Cristian", "Darlan", "Diogo", "Gomes", "João", "Luciano", "Lucas", "Gustavo", "Juliano", "Marcos", "Roberto", "Rovilso", "Bruno", "Eduardo", "Eric", "Felipe", "Idevaldo", "Julian", "Laura", "Rizzi", "Rafael"]
numRam = ["3016", "3119", "3234", "3233", "3317", "3317", "3218", "3235", "3617", "3120", "3417", "3262", "3216", "3217", "3319", "3116", "3428", "3018", "3261", "3619", "3418", "3419", "3620", "3019", "3618"]
depRam = ["Melhoria", "DEV", "Teste", "Infra", "Suporte"]
def encontraRamal(infoEsp, y, ramalEncontrado, namRam):  
    if infoEsp in nomes:
        while y < 25:
            if infoEsp == namRam[y].nomeRamal:
                ramalEncontrado = (y)
            y += 1
    print(namRam[ramalEncontrado].nomeRamal, namRam[ramalEncontrado].numRamal)

while x < len(namRam):
    namRam[x] = Ramais(nomeRamal = namRam[x], numRamal=numRam[x], depRamal="NA")
    x += 1

while priVal == False:
    utilidade = input("Digite a funcionalidade que deseja: Programas Uteis (PU), Filiais (F), Ramais (R)\n")
    utilidade = utilidade.upper()
    if utilidade == ("PU"):
        for li in (proUtiOps):
            print (li)
        proUti = input("Digite o que precisa saber: ")
        if proUti == ("1"):
            clear
            print ("Acesse o ZIM")
            print ("Acesse o acesso rapido apertando F2")
            print ("Acesse a opção 2")
            print ("Digite a filial de emissão do CT-e e o numero do conhecimento")
            print ("Aperte END + F10")
        elif proUti == ("2"):
            print ("Acesse o ZIM")
            print ("Acesse o acesso rapido apertando F2")
            print ("Acesse a opção 16")
            print ("Digite o CNPJ do cliente")
    elif utilidade == ("F"):
        info = input ("Digite se quer todas as filiais ou uma especifica (T) ou (E): ")
        info = info.upper()
        x = 0
        if info == ("T"):
            while x < 25:
                print (codFiliais [x], filiais[x], cnpjFiliais[x])
                x += 1
        elif info == ("E"):
            infoEsp = input ("Pesquisa por Codigo da Filial (C), Nome da Filial (N), Sigla da Filial (S) ou CNPJ (CN): ")
            infoEsp = infoEsp.upper()
            if infoEsp == ("C"):
                infoCodFil = input ("Digite o numero da Filial: ")
                encontraFilial(infoCodFil, codFiliais,0, idFiliais, filiais, cnpjFiliais,0,codFiliais)
            elif infoEsp == ("N"):
                infoCodFil = input ("Digite o nome da Filial: ")
                infoCodFil = infoCodFil.title()
                print (infoCodFil)
                encontraFilial(infoCodFil, codFiliais,0, idFiliais, filiais, cnpjFiliais,0,filiais)
            elif infoEsp == ("S"):
                infoCodFil = input ("Digite a sigla da Filial: ")
                infoCodFil = infoCodFil.upper()
                encontraFilial(infoCodFil, codFiliais,0, idFiliais, filiais, cnpjFiliais,0,idFiliais)
            elif infoEsp == ("CN"):
                infoCodFil = input ("Digite o CNPJ da Filial: ")
                encontraFilial(infoCodFil, codFiliais,0, idFiliais, filiais, cnpjFiliais,0,cnpjFiliais)   
        else:
            print ("Opção invalida")
    elif utilidade == ("R"):
        info = input ("Digite se quer todos ramais ou um especifico (T) ou (E): ")
        info = info.upper()
        x = 0
        if info == ("T"):
            while x < len(namRam):
                print (namRam[x].nomeRamal, namRam[x].numRamal)
                x += 1
        elif info == ("E"):
            infoEsp = input ("Digite o nome da pessoa que deseja o ramal: ")
            infoEsp = infoEsp.title()
            print (infoEsp)
            encontraRamal(infoEsp, 0, 0, namRam)
