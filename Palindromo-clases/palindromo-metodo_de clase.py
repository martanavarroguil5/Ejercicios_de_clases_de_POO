class Palíndromo():
    
    #constructor
    def __init__ (self, palabra):
        self.palabra = palabra

    #getter
    def get_palabra(self):
        return self.palabra
    

    def es_palindromo(self):
        # Pone en minusculas y la agupa para evaluar solo los simbolos y no los espacios.
        palabra = self.palabra.replace(' ', '').lower()
        if palabra == palabra [::-1]:
            return True 
        else:
             return False# compara la palabra y la palabra escrita del revés
    
    # Respuesta a las palabras palíndromas o no.
    def resultado(self):
        if self.es_palindromo == True:
            return f'La palabra {self.palabra} es un palíndromo.'
        else:
            return f'La palabra {self.palabra} no es un palíndromo'

    '''def __str__(self):
        return self.resultado()'''
    
def main():
        '''palabra = input('Escribe una palabra: ')
        palindromo = palabra.es_palindromo()
        print(palindromo)'''

        palabra1 = Palíndromo('COlarDO')
        palabra2 = Palíndromo('MEGUSTAtsugem')
        palabra3 = Palíndromo('lao o al')

        print(palabra1.es_palindromo())
        print(palabra1.resultado())

'''def test(self):
        return (self.es_palindromo(), self.palabra.upper())'''

if __name__ == "__main__":
    main()
    




