from django.db import models

# Create your models here.
class Libro(models.Model):
    class Meta:
        ordering = ["titulo"]
        verbose_name_plural = "Libros"

    class Genero(models.TextChoices):
        NOVELA = "NOV", "Novela"
        POESIA = "POE", "Poesía"
        TEATRO = "TEA", "Teatro"
        ENSAYO = "ENS", "Ensayo"
        COMIC = "COM", "Cómic"

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(
            max_length=3,
            choices=Genero.choices,
            default=Genero.NOVELA,
        )
    anio_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)
    

    def __str__(self) -> str:
        return f"{self.titulo} ({self.autor})"

    