from cgitb import text
from glob import glob
from re import L
from tkinter import *
from asyncore import read, write
from datetime import datetime
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Leitor de Arquivos EDI - Posicoes conforme PROCEDA!")
#root.iconbitmap("C:/DEV/StudioCode/Gerador.ico")
root.geometry("700x350")

quantidadeLinhas_arquivo = 0
linhasArquivo = []


def escolheArquivo():
    global quantidadeLinhas_arquivo
    global linhasArquivo
    global registro_entrada
    global posicaoInicial_entrada
    global posicaoFinal_entrada
    caminhoEspecificado = askopenfilename()
    print (caminhoEspecificado)
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

def confirmaDados():
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
    registroEncontrado = Text(telaDados)
    registroEncontrado.grid(row=0, column=0)
    print (linhasArquivo)
    contadorTag = 1.0
    for linha in linhasArquivo:
        if registro in linha[0:3]:
            registroEncontrado.insert(INSERT, linha + "\n")
            registroEncontrado.tag_add("registro", contadorTag, contadorTag + 0.3)
            registroEncontrado.tag_config("registro", background="yellow")
            contadorPosicao = str(contadorTag)
            contadorPosicao = contadorPosicao[:-2]
            print (contadorPosicao + posicaoInicial)
            print (contadorPosicao + posicaoFinal)
            contadorTag = contadorTag + 1
            registroEncontrado.tag_add("posicao", contadorPosicao + posicaoInicial, contadorPosicao + posicaoFinal)
            registroEncontrado.tag_config("posicao", background="red")
            
#Layouts
telaInicial = LabelFrame(root, text="Tela inicial")
telaInicial.grid(row=0, column=0)

telaDados = LabelFrame(root, text="Dados Destacados")

definirInformações = LabelFrame(root,text="Registro e Posições")

#Botões
entradaArquivo_botao = Button(telaInicial, text="Escolha o arquivo", command=escolheArquivo)
entradaArquivo_botao.grid(row=0, column=0)

root.mainloop()