from django.contrib import admin
from .models import Autor, Editorial, Libro, Participacion, Prestamo

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Participacion)
admin.site.register(Prestamo)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "isbn", "precio", "disponible", "editorial")
    list_filter = ("disponible", "editorial")
    search_fields = ("titulo", "isbn", "autores__nombre")
    ordering = ("titulo",)
    list_per_page = 20