from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Definisci un inline admin per il profilo utente
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profilo Utente'

# Estendi l'admin del modello User per includere il profilo utente
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Deregistra il modello User standard e registra il nuovo
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
