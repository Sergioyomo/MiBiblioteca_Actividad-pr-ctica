from django.db import models
from django.conf import settings

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True)
    sitio_web = models.URLField(blank=True)
    activa = models.BooleanField(blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}"


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

    class Dificultad(models.IntegerChoices):
        BASICA = 1, "Básica"
        INTERMEDIA = 2, "Intermedia"
        AVANZADA = 3, "Avanzada"


    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13 , unique=True)
    idioma = models.CharField(max_length=30, default="Español")
    sinopsis = models.TextField(blank=True)
    autores = models.ManyToManyField(
        "Autor",
        through="Participacion",
        related_name="libros",
        blank=True,
    )

    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.PROTECT,
        related_name="libros",
        null=True,
        blank=True,
    )
    fecha_publicacion = models.DateTimeField()
    paginas = models.PositiveIntegerField()
    precio =models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    genero = models.CharField(
            max_length=3,
            choices=Genero.choices,
            default=Genero.NOVELA,
    )
    dificultad = models.IntegerField(
        choices=Dificultad.choices,
        default=Dificultad.BASICA,
    )
    recomendado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo

class Participacion(models.Model):
    class Funcion(models.TextChoices):
        PRINCIPAL = "PRI", "Autor principal"
        COAUTOR = "COA", "Coautor"
        COLABORADOR = "COL", "Colaborador"

    libro = models.ForeignKey(
        "Libro", on_delete=models.CASCADE, related_name="participaciones"
    )
    autor = models.ForeignKey(
        "Autor", on_delete=models.CASCADE, related_name="participaciones"
    )
    funcion = models.CharField(
        max_length=3, choices=Funcion.choices, default=Funcion.COAUTOR
    )
    fecha_incorporacion = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["libro", "autor"], name="participacion_unica_libro_autor"
            )
        ]

    def __str__(self) -> str:
        return f"{self.autor} - {self.libro} ({self.get_funcion_display()})"

class Prestamo(models.Model):
    libro = models.ForeignKey(
        "Libro", on_delete=models.PROTECT,
        related_name="prestamos"
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="prestamos_biblioteca"
    )
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Préstamo {self.pk}: {self.libro}"
