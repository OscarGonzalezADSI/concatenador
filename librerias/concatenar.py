"""
OscarGonzalez1987/concatenador is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license notices 
must be preserved. Contributors provide an express grant of patent rights.
"""

def concatenar(archivo, nombre, variable):

    def ejecutar(archivo, nombre, variable):
        leer = open(archivo, "r")
        inicia_concatenado(nombre, variable)
        ciclo_lecto_escritura(variable, leer)
        leer.close()
        
    def inicia_concatenado(nombre, variable):   
        escribe = open(nombre, "w")
        escribe.write(variable + " = \"\"\n")
        escribe.close()
    
    def ciclo_lecto_escritura(variable, leer):
        nro_lineas = consulta_de_lineas(archivo, leer)
        nn=0
        while(nro_lineas > nn):
            #-------------------------------------
            toma = leer.readline()
            contenido = toma.replace("\"", "\\\"").rstrip("\n")
            escribe_ciclo(variable, contenido)
            #-------------------------------------
            nn+=1
        write_print(variable+"\n")
        
    def consulta_de_lineas(archivo, leer):
        nro_lineas = len(leer.readlines())
        leer.seek(0)
        return nro_lineas
        
    def escribe_ciclo(variable, contenido):    
        escribe = open(nombre, "a")
        escribe.write(variable + " += \"" + contenido + "\\n\"\n")
        escribe.close()
        
    def write_print(variable):    
        escribe = open(nombre, "a")
        escribe.write("print("+ variable.rstrip("\n") +")\nfin = input("")")
        escribe.close()
        
    ejecutar(archivo, nombre, variable)
    
    

"""
#-------------------------------------
# ejemplo de uso en otro archivo (.py):
#-------------------------------------
import librerias.concatenar as lbr

archivo = "plantillas/tabla.html"
nombre = "productos/resultado.py"
variable = "variable"
lbr.concatenar(archivo, nombre, variable)
"""















