#-------------------------------------
# ejemplo de uso:
#-------------------------------------
import librerias.concatenar as lbr

archivo = "plantillas/tabla.html"
nombre = "productos/resultado.py"
variable = "variable"
lbr.concatenar(archivo, nombre, variable)

#------------------------------------------------------------------
fin = input("\nEjecución completada.\n"+
            "--------------------------------------------------\n"+
            "Por favor revice \""+ nombre +"\"\n"
            "y compruebe que el archivo fue creado exitosamente.\n")

















