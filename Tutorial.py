class EDI(object):
    def __init__(self, tpArqv):
        self.tpArqv = tpArqv

Tramontina = EDI(tpArqv="CONEMB")
Beirario = EDI(tpArqv="DOCCOB")

print (Tramontina.tpArqv)
print (Beirario.tpArqv)

help(len)