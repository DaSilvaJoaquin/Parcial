






#Punto 1
contadorr= 0
vectorr=['arroz','pan' ,'arroz', 'arroz', 'pan']
def cantidadpalabra(vector,palabra,contador): 
    if len(vector) == 0:
        print (contador)
    else :
        if vector[0]== palabra :
            contador = contador+1
            return cantidadpalabra(vector[1:],palabra,contador)
        else:                    
            return cantidadpalabra(vector[1:],palabra,contador)

cantidadpalabra(vectorr,'arroz',contadorr)

#Punto 2
 
from pila import Pila
from cola import Cola
class Superheroes():
    def __init__(self, nombre_superheroe, nombre_personaje, grupo , anio_aparicion):
        self.__nombre_superheroe = nombre_superheroe
        self.__nombre_personaje = nombre_personaje
        self.__grupo = grupo
        self.__anio_aparicion = anio_aparicion   
    def get_nombresuperheroe(self):
        return self.__nombre_superheroe
    
    def get_nombrepersonaje(self):
        return self.__nombre_personaje
    
    def get_grupo(self):
        return self.__grupo
    
    def get_anioaparicion(self):
        return self.__anio_aparicion
    def change_nombresuperheroe(self,new_name):
        self.__nombre_superheroe= new_name
Superheros=[
    Superheroes('Rocket Racoon','','Guardianes de la Galaxia', 1976),
    Superheroes('Loki','','',1949),
    Superheroes('Hulk','Bruce Banner','The Avengers',1962),
    Superheroes('Black Cat','Felicia Hardy','Heroes de Alquiler',1979)
    ]
Superrheroes=[
    Superheroes('Iron Man', 'Tony Stark', 'The Avengers', 1963),
    Superheroes('Vlanck Widow','Natasha Romanoff','The Avengers', 1964),
    Superheroes('Hulk','Bruce Banner', 'The Avengers', 1962),
    Superheroes('Dr.Strange','Stephen Vicent Strange','Illuminati',1963),
    Superheroes('Wolverine','James Howlett', 'X-Men',1974),
    Superheroes('Spider-Man','Peter Parker','',1962),
    Superheroes('Hawkeye','Clinton Francis','The Avengers',1964),
    Superheroes('Star Lord','Peter Quill','Guardianes de la Galaxia',0),
    Superheroes('Capitana Marvel','Carol Danvers','The Avengers',1968),
    Superheroes('Black Panther','Tchala','The Avengers',1966),
    Superheroes('Scarlett Witch','Wanda Maximoff','The Avengers',1964),
    Superheroes('Ant-Man','Hank Pym','The Avengers',1962),
    Superheroes('Groot','','Guardianes de la Galaxia',1960),
    Superheroes('Gamora','Gamora Zen Whoberi Ben Titan','Guardianes de la Galaxia',1975),
    Superheroes('Capitan America','Steven Rogers','The Avengers',1941),
    Superheroes('Thor','Donald Blake','The Avengers',1962),
    Superheroes('Vision','','The Avengers',1968),   
]

pila_1 = Pila()
cola_1= Cola()
lista_1= Lista()
lista_2= Lista()
for i in range(0,len(Superheros)-1):
   if Superheros[i].get_nombresuperheroe() in Superrheroes:
       print('Ya se encuentra en la lista')
   else:
       Superrheroes.append(Superheros[i])          
for Superheroes in Superrheroes :
    pila_1.push(Superheroes)
    while pila_1.size ()>0:
        dato=pila_1.pop()
        if dato.get_nombresuperheroe()== 'Vlanck Widow':
            dato.change_nombresuperheroe('Black Widow')
        if dato.get_nombresuperheroe() == 'Capitana Marvel':
            print(dato.get_nombrepersonaje())
        
         if dato.get_grupo()== 'Guardianes de la Galaxia':
             cola_1.arrive(dato)
        if (dato.get_anioaparicion()>1960) and (dato.get_nombrepersonaje !=''):
            print('Aparecio despues de 1960 ',dato.get_nombresuperheroe())
         if (dato.get_nombrepersonaje()[0:1]=='C') or (dato.get_nombrepersonaje()[0:1]=='P') or (dato.get_nombrepersonaje()[0:1]=='S'):
             print('Empieza por C,P o S ',dato.get_nombrepersonaje())
 print('Cantidad de Guardianes de la Galaxia en la lista', cola_1.size())

#Punto 3
class Misiones():
    def __init__(self,planeta_visitado,captura,costo):
        self.__planeta_visitado = planeta_visitado
        self.__captura = captura
        self.__costo = costo
        
    def get_planeta_visitado(self):
        return self.__planeta_visitado
    
    def get_captura(self):
        return self.__captura
    
    def get_costo(self):
        return self.__costo


pila_2 = Pila()
missions=[
    
    Misiones('Alderaan', 'Anakin Skywolker', 2000000),
    Misiones('Yavin IV', 'Obi-Wan Kenobi', 10000000),
    Misiones('Tatooine', 'Hans Solo', 13000),
]
for Misiones in missions:
    pila_2.push(Misiones)
pila_3= Pila()
creditos=0
cntador=0
while pila_2.size()>0:
    dato1=pila_2.pop()
    pila_3.push(dato1)
    creditos= creditos + (dato1.get_costo())

print('El total de creditos acumulados es :$ ', creditos)
while pila_3.size()>0:
    dato2=pila_3.pop()
    cntador=cntador + 1
    print(dato2.get_planeta_visitado())
    if dato2.get_captura()== 'Hans Solo':
        print('Hans Solo fue capturado en la mision ', cntador,' en el planeta ', dato2.get_planeta_visitado())
    