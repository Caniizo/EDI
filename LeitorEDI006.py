from cgitb import text
from decimal import ROUND_05UP
from glob import glob
from re import L
from tkinter import *
from asyncore import read, write
from datetime import datetime
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Leitor de Arquivos EDI - Posicoes conforme PROCEDA!")

quantidadeLinhas_arquivo = 0
linhasArquivo = []

def escolheArquivo(): # Informar posições manuais!
    global quantidadeLinhas_arquivo
    global linhasArquivo
    global registro_entrada
    global posicaoInicial_entrada
    global posicaoFinal_entrada
    caminhoEspecificado = askopenfilename()
    leitorArquivo = open(caminhoEspecificado, "r")
    telaInicial.grid_forget()
    for linha in leitorArquivo:
        entradaArquivo_botao.grid_forget() # Esquece o botão principal
        linha_temporaria = linha[0:(len(linha)) - 1]
        linhasArquivo.append(linha_temporaria) # Vincula a linha em questão com a lista
        linhasArquivo[quantidadeLinhas_arquivo]
        quantidadeLinhas_arquivo = quantidadeLinhas_arquivo + 1 # Sobe o contador
    definirInformações.grid(row=quantidadeLinhas_arquivo + 1, column=0)
    
    registro_texto = Label(definirInformações, text="Registro")
    registro_texto.grid(row=0, column=0)
    registro_entrada = Entry(definirInformações, width=15)
    registro_entrada.grid(row=0, column=1)

    posicaoInicial_texto = Label(definirInformações, text="Posição Inicial")
    posicaoInicial_texto.grid(row=1, column=0)
    posicaoFinal_texto = Label(definirInformações, text="Posição Final")
    posicaoFinal_texto.grid(row=2, column=0)
    posicaoInicial_entrada = Entry(definirInformações, width=15)
    posicaoInicial_entrada.grid(row=1, column=1)
    posicaoFinal_entrada = Entry(definirInformações, width=15)
    posicaoFinal_entrada.grid(row=2, column=1)

    confirma_botao = Button(definirInformações, text="Confirmar", command=confirmaDados)
    confirma_botao.grid(row=3, column=0)

def confirmaDados(): # Informações para posição e registro manuais!!!
    definirInformações.grid(row=0, column=0)
    telaDados.grid(row=0, column=1)
    registro = registro_entrada.get()
    registro = str(registro)
    posicaoInicial = posicaoInicial_entrada.get()
    posicaoInicial = int(posicaoInicial) -1
    posicaoInicial = str(posicaoInicial)
    posicaoInicial = "." + posicaoInicial
    posicaoFinal = posicaoFinal_entrada.get()
    posicaoFinal = "." + posicaoFinal
    registroEncontrado = Text(telaDados, wrap=NONE)
    registroEncontrado.grid(row=0, column=0)
    contadorTag = 1.0
    for linha in linhasArquivo:
        if registro in linha[0:3]:
            registroEncontrado.insert(INSERT, linha + "\n")
            registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
            registroEncontrado.tag_config("registro", background="yellow")
            contadorPosicao = str(contadorTag)
            contadorPosicao = contadorPosicao[:-2]
            contadorTag = contadorTag + 1
            registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal)
            registroEncontrado.tag_config("posicao", background="red")

def confirmaDados_conemb(): #Ira jogar na tela o valor selecionado no DROPDOWN dos dados do CONEMB
    
    if "520CONHE" in linhasArquivo[1]: # Valida se é um CONEMB com base na informação dentro do arquivo   
        if configDropdown.get() == "Numero do CT-e":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "522"
            posicaoInicial = ".18"
            posicaoFinal = ".24"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")
        elif configDropdown.get() == "Data de Emissão do CT-e":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "522"
            posicaoInicial = ".30"
            posicaoFinal = ".38"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")
        elif configDropdown.get() == "Notas Fiscais":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "524"
            posicaoInicial = ".17"
            posicaoFinal = ".27"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")
        elif configDropdown.get() == "Valor do CT-e":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "523"
            posicaoInicial = ".40"
            posicaoFinal = ".55"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")
    elif "320CONHE" in linhasArquivo[1]: # Configuração 3.0
        if configDropdown.get() == "Numero do CT-e":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "322"
            posicaoInicial = ".18"
            posicaoFinal = ".24"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal)
                    registroEncontrado.tag_config("posicao", background="red")    
        elif configDropdown.get() == "Data de Emissão do CT-e":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "322"
            posicaoInicial = ".30"
            posicaoFinal = ".38"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")
        elif configDropdown.get() == "Notas Fiscais":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "322"
            posicaoInicial = ".235"
            posicaoFinal = ".243"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")
        elif configDropdown.get() == "Valor do CT-e":
            definirInformações.grid(row=0, column=0)
            telaDados.grid(row=0, column=1)
            registro = "322"
            posicaoInicial = ".46"
            posicaoFinal = ".61"
            registroEncontrado = Text(telaDados, wrap=NONE)
            registroEncontrado.grid(row=0, column=0)
            contadorTag = 1.0    
            for linha in linhasArquivo:
                if registro in linha[0:3]:
                    registroEncontrado.insert(INSERT, linha + "\n")
                    registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                    registroEncontrado.tag_config("registro", background="yellow")
                    contadorPosicao = str(contadorTag)
                    contadorPosicao = contadorPosicao[:-2]
                    contadorTag = contadorTag + 1
                    registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                    registroEncontrado.tag_config("posicao", background="red")

def confirmaDados_notfis(): #Ira jogar na tela o valor selecionado no DROPDOWN dos dados do NOTFIS
    if configDropdown.get() == "Numero da NF-e":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "505"
        posicaoInicial = ".6"
        posicaoFinal = ".15"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal)
                registroEncontrado.tag_config("posicao", background="red")    
    elif configDropdown.get() == "Data de Emissão da NF-e":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "505"
        posicaoInicial = ".15"
        posicaoFinal = ".23"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")
    elif configDropdown.get() == "Valor da NF-e":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "506"
        posicaoInicial = ".66"
        posicaoFinal = ".81"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")
    elif configDropdown.get() == "Cubagem":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "506"
        posicaoInicial = ".39"
        posicaoFinal = ".49"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")

def confirmaDados_ocorren():#Ira jogar na tela o valor selecionado no DROPDOWN dos dados do OCORREN
    if configDropdown.get() == "Numero da NF-e":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "542"
        posicaoInicial = ".20"
        posicaoFinal = ".29"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal)
                registroEncontrado.tag_config("posicao", background="red")    
    elif configDropdown.get() == "Data da Ocorrencia":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "542"
        posicaoInicial = ".32"
        posicaoFinal = ".40"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")
    elif configDropdown.get() == "Código da Ocorrencia":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "542"
        posicaoInicial = ".29"
        posicaoFinal = ".32"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")

def confirmaDados_doccob():#Ira jogar na tela o valor selecionado no DROPDOWN dos dados do DOCCOB
    if configDropdown.get() == "Numero da Fatura":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "552"
        posicaoInicial = ".17"
        posicaoFinal = ".27"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal)
                registroEncontrado.tag_config("posicao", background="red")    
    elif configDropdown.get() == "Data de Vencimento":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "552"
        posicaoInicial = ".35"
        posicaoFinal = ".43"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")
    elif configDropdown.get() == "Valor da Fatura":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "552"
        posicaoInicial = ".43"
        posicaoFinal = ".58"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")
    elif configDropdown.get() == "Numero do CT-e":
        definirInformações.grid(row=0, column=0)
        telaDados.grid(row=0, column=1)
        registro = "555"
        posicaoInicial = ".18"
        posicaoFinal = ".24"
        registroEncontrado = Text(telaDados, wrap=NONE)
        registroEncontrado.grid(row=0, column=0)
        contadorTag = 1.0    
        for linha in linhasArquivo:
            if registro in linha[0:3]:
                registroEncontrado.insert(INSERT, linha + "\n")
                registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
                registroEncontrado.tag_config("registro", background="yellow")
                contadorPosicao = str(contadorTag)
                contadorPosicao = contadorPosicao[:-2]
                contadorTag = contadorTag + 1
                registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal) 
                registroEncontrado.tag_config("posicao", background="red")

def versao50(): # Ao Selecionar a Opção "Identificar Automaticamente" na Tela Inicial
    global quantidadeLinhas_arquivo
    global linhasArquivo
    global registro_entrada
    global posicaoInicial_entrada
    global posicaoFinal_entrada
    caminhoEspecificado = askopenfilename()
    leitorArquivo = open(caminhoEspecificado, "r")
    telaInicial.grid_forget()
    for linha in leitorArquivo:
        linha_temporaria = linha[0:(len(linha)) - 1]
        linhasArquivo.append(linha_temporaria) # Vincula a linha em questão com a lista
        linhasArquivo[quantidadeLinhas_arquivo]
        quantidadeLinhas_arquivo = quantidadeLinhas_arquivo + 1 # Sobe o contador
    
    definirInformações.grid(row=quantidadeLinhas_arquivo + 1, column=0)
    
    if "CONHE" in linhasArquivo[1]: # Identifica que o arquivo é um CONEMB e jogar as opções presetadas do DROPDOWN
        descricaoLayout = ["Numero do CT-e", "Data de Emissão do CT-e", "Valor do CT-e", "Notas Fiscais"] # Dropdown do Conemb
        dropdownLayout = OptionMenu(definirInformações, configDropdown, *descricaoLayout)
        dropdownLayout.grid(row=3, column=0)
        confirma_botao = Button(definirInformações, text="Confirmar", command=confirmaDados_conemb)
        confirma_botao.grid(row=4, column=0)
    elif "540OCO" in linhasArquivo[1]: # Identifica que o arquivo é um OCORREN e jogar as opções presetadas do DROPDOWN
        descricaoLayout = ["Numero da NF-e", "Data da Ocorrencia", "Código da Ocorrencia"] # Alterando informações do DROPDOWN para dados de NOTFIS
        configDropdown.set("Numero da NF-e") 
        dropdownLayout = OptionMenu(definirInformações, configDropdown, *descricaoLayout)
        dropdownLayout.grid(row=3, column=0) # Colocando dropdown na tela
        confirma_botao = Button(definirInformações, text="Confirmar", command=confirmaDados_ocorren) # Botão de confirmação
        confirma_botao.grid(row=4, column=0) # Colocando na tela
    elif "550COB" in linhasArquivo[1]:
        descricaoLayout = ["Numero da Fatura", "Data de Vencimento", "Valor da Fatura", "Numero do CT-e"] # Alterando informações do DROPDOWN para dados de NOTFIS
        configDropdown.set("Numero da Fatura") 
        dropdownLayout = OptionMenu(definirInformações, configDropdown, *descricaoLayout)
        dropdownLayout.grid(row=3, column=0) # Colocando dropdown na tela
        confirma_botao = Button(definirInformações, text="Confirmar", command=confirmaDados_doccob) # Botão de confirmação
        confirma_botao.grid(row=4, column=0) # Colocando na tela
    elif "500NOT" in linhasArquivo[1]:

        descricaoLayout = ["Numero da NF-e", "Data de Emissão da NF-e", "Valor da NF-e", "Cubagem"] # Alterando informações do DROPDOWN para dados de NOTFIS
        configDropdown.set("Numero da NF-e") 
        dropdownLayout = OptionMenu(definirInformações, configDropdown, *descricaoLayout)
        dropdownLayout.grid(row=3, column=0) # Colocando dropdown na tela
        confirma_botao = Button(definirInformações, text="Confirmar", command=confirmaDados_notfis) # Botão de confirmação
        confirma_botao.grid(row=4, column=0) # Colocando na tela
    else:
        linhasArquivo.clear()
        quantidadeLinhas_arquivo = 0
        telaInicial.grid(row=0, column=0)
        Label(telaInicial, text="Arquivo invalido...").grid(row=3, column=0)
        Label(telaInicial, text="Somente Proceda 5.0").grid(row=4, column=0)
            
#Layouts
telaInicial = LabelFrame(root, text="Tela inicial")
telaInicial.grid(row=0, column=0)

telaDados = LabelFrame(root, text="Dados Destacados")

definirInformações = LabelFrame(root,text="Registro e Posições")

#OpcoesDropdown
configDropdown = StringVar()
configDropdown.set("Numero do CT-e")

#Dropdown


#Botões
entradaArquivo_botao = Button(telaInicial, text="Escolha o arquivo para procurar manualmente posições", command=escolheArquivo)
entradaArquivo_botao.grid(row=0, column=0)

proceda50 = Button(telaInicial, text="Identificar Automaticamente", command=versao50)
proceda50.grid(row=2, column=0)

#Textos
texto1 = Label(telaInicial, text="OU")

texto1.grid(row=1, column=0)

root.mainloop()