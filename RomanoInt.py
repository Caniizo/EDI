listaRomanos = ["I", "V", "X"] # Define os possiveis valores que o usuario ira declarar
valorRomanos = [1, 5, 10] # Define os valores que o usuario declarou

valorUsuario = input("Digite um valor Romano: ") # Pega o Input do usuario
valorUsuario = valorUsuario.upper() #Transforma em maiusculo

contador = 0 # Inicia um contador zerado

ultimoValor = "Nada" # Define uma variavel com valor "nulo"

tamanhoString = 0 # Define a posição da lista

for x in valorUsuario: # for para rodar toda a string
	if contador == 0: # SEMPRE ira pegar o primeiro caractere, pois o contador sempre inicia zerado
		if x in listaRomanos: # Se o valor da primeira String estiver dentro da listaRomanos
			contador = valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])]
	elif contador !=0:
		if x in listaRomanos:
			if valorUsuario[tamanhoString] == "I":
				ultimoValor = valorUsuario[tamanhoString]
				contador = contador + 1
			elif ultimoValor == "I" and valorUsuario[tamanhoString] != "I":
				## contador =  -11
				contador = contador + valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])]
				ultimoValor = "Nada"
				contador = contador - 2			

			elif valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])] > contador:
				contador = valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])] - contador
			elif valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])] < contador:
				contador = valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])] + contador
			elif valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])] == contador:
				contador = valorRomanos[listaRomanos.index(valorUsuario[tamanhoString])] + contador
	tamanhoString +=1

print ("O valor é de " + str(contador))
input ("Vai ter que reabrir, preguiça de fazer while nisso")