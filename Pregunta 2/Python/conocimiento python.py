#Test de conocimiento, Python .... recorrer un arreglo de tamaño 10[0,1,2,3,4,5,6,7,8,9]

#Ya que en python no existen los arreglos, crearemos una lista como tupla ya que son tipos de datos estaticos

tupla = (0,1,2,3,4,5,6,7,8,9)

#recorremos la tupla
print("Tupla")
for x in tupla:
    print(x)

print("********************")
#En caso de que se pidiera una lista

list = [0,1,2,3,4,5,6,7,8,9]

#también se puede recorrer de manera diferente...
print("Lista")
for x in range(len(list)):
    print("index = " + str(x)+ " tiene", list[x])



input()
    


