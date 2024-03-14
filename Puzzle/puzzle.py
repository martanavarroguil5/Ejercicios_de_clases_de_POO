'''
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z')))'''


#Primero creo la clase objeto.
class Objeto:  
    #creamos el constructor con el atributo atributo que se utilizará en el método_y
    def __init__(self, atributo = None): #Esto permite crear instancias de la clase sin pasar ningún argumento
        
        self.atributo = atributo

    # Renombre los métodos y sus atributos para ser mas claro  
    def metodo_z(self): 
        return self 
    
    def metodo_y(self, atributo=None):
        if atributo is None:
            atributo = self.atributo
        if atributo is None:
            return 0 
        return len(atributo)
 


# Asignamos nombres a las variables adecuadas y nombramos a los métodos   
instancia_a = Objeto()
resultado1 = instancia_a.metodo_z()
print(resultado1)

# Crear otra instancia de Clase Objeto y comprobar si es la misma que la anterior
instancia_aa = Objeto()
print(instancia_aa is instancia_a)

#Llamada al método metodo_y de la instancia_aa con una lista vacía
resultado2 = instancia_aa.metodo_y()
print(resultado2)

# Creo una instancia más de tipo Objeto que es una tupla que continela clase Objeto
instancia_3 = Objeto().metodo_y((Objeto,))
print(instancia_3) 

#Otra instancia de tipo objeto que consiste en una tupla que contiene la clase Objeto  y el metodo_z
instancia_4 = Objeto().metodo_y((Objeto, Objeto.metodo_z,))
print(instancia_4) 

# Creo otra instancia de tipo objeto que contiene 3 elementos diferentes
instancia_5 = Objeto().metodo_y((Objeto.metodo_z, 1, 'z',))
print(instancia_5)