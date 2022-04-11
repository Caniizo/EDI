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

while priVal == False:
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
            encontraFilial(infoCodFil, codFiliais,-1, idFiliais, filiais, cnpjFiliais,-1,codFiliais)
        elif infoEsp == ("N"):
            infoCodFil = input ("Digite o nome da Filial: ")
            infoCodFil = infoCodFil.title()
            print (infoCodFil)
            if infoCodFil in filiais:
                while x <25:
                    if infoCodFil == filiais[x]:
                        filialEncontrada = (x)
                    x += 1
                print (codFiliais[filialEncontrada],idFiliais[filialEncontrada], filiais[filialEncontrada], cnpjFiliais[filialEncontrada])
        elif infoEsp == ("S"):
            infoCodFil = input ("Digite a sigla da Filial: ")
            infoCodFil = infoCodFil.upper()
            if infoCodFil in idFiliais:
                while x <25:
                    if infoCodFil == idFiliais[x]:
                        filialEncontrada = (x)
                    x += 1
                print (codFiliais[filialEncontrada],idFiliais[filialEncontrada], filiais[filialEncontrada], cnpjFiliais[filialEncontrada])
        elif infoEsp == ("CN"):
            infoCodFil = input ("Digite o CNPJ da Filial: ")
            encontraFilial(infoCodFil, codFiliais,0, idFiliais, filiais, cnpjFiliais,0,cnpjFiliais)   
        else:
            print ("Opção invalida")
