from django.contrib import admin

from .models import Tblmacchine  # Assicurati che l'import sia corretto

@admin.register(Tblmacchine)
class TblmacchineAdmin(admin.ModelAdmin):
    list_display = ('idmacchina', 'descrizione', 'id_tipo_macchina')  # Mostra questi campi nell'elenco admin
