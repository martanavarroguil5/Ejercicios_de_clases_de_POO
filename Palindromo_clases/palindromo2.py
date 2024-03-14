class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.atributo = palabra  # Nuevo atributo para almacenar la palabra inicial

    #getter
    def get_palabra(self):
        if isinstance(self.palabra, str):
            return self.palabra
        else:
            raise TypeError("La palabra debe ser una cadena de texto.")

    def es_palindromo(self):
        palabra = self.palabra.replace(' ', '').lower()
        return palabra == palabra[::-1]

    def resultado(self):
        if self.es_palindromo():
            return f'La palabra {self.palabra} es un palíndromo.'
        else:
            return f'La palabra {self.palabra} no es un palíndromo.'

    def test(self):
        return self.es_palindromo()

    def __del__(self):
        print(self.atributo.upper())  # cuando se  destruye la instancia, muestra el atributo en mayúsculas


p1 = Palindromo("radar")
print(p1.test()) 
p2 = Palindromo("sonar")
del p2  # Al destruir p2, mostrará "SONAR"
#print(p2.test())  # Esto lanzará un error porque p2 ya no existe
