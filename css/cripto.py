#Criptando


 
frase= "Meu nome não é joseph"
mensagem = ""

def criptografar (frase):
    for i in frase:
    mensagem = mensagem + chr ( ord(i) + 7)
 return frase 

print (criptografar ("Meu nome não é Jaiminho "))

