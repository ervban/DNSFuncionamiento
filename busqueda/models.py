from django.db import models

class Paginas(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=30)
    ip_nombre = models.CharField(max_length=15)
    

    #Redefinir metodo de str
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.Nombre, self.ip_nombre)