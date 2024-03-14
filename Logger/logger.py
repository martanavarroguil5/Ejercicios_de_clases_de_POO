#Creamos la clase Logger y su constructor
class Logger:
    def __init__(self, filename): # Message no esta en el constructor porque el mensaje puede cambiar con el método log
        self.filename = filename
        self.log_count = 0

    # Getter
    def get_filename(self):
        if isinstance(self.filename, str):
            return self.filename
        else:
            raise TypeError("El nombre del archivo debe ser una cadena de texto.")
    

    
    # Se abre un archivo del nombre especificado con self.filename. ¨a'sirve para adjuntar en el caso de renombrar
    def log(self, message):
        with open(self.filename, 'a') as file:
            if self.log_count == 0:
                file.write("--Start log--" + '\n')
 
            # Añadir al archivo un mensaje
            file.write(message + '\n')
            # Añadir al contador 1 itinerancia
            self.log_count += 1

    # Se crea la clase close que se llama cuando se termina de introducir los mensajes, le añade el contador        
    def close(self):
        with open(self.filename, 'a') as file:
            file.write(f"--End log: {self.log_count} log(s) --\n")

        
logger1 = Logger('Marta')
logger1.log('me gsta el brocoli')
logger1.close()
