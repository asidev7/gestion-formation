from django.contrib import admin
from django.urls import path
from .models import Formation, Client, Inscription, Session, Specialite, Instructeur, Categorie, Personnel
from django.template.response import TemplateResponse
from django.db import models


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'instructeur')
    list_filter = ('categorie', 'instructeur')
    search_fields = ('titre', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email')
    search_fields = ('nom', 'email')

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('client', 'get_session', 'date_inscription')  # Corrected list_display
    search_fields = ('client__nom', 'session__formation__titre')

    def get_session(self, obj):
        return obj.session

    get_session.short_description = 'Session'

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('formation', 'date_debut', 'date_fin', 'lieu')

@admin.register(Specialite)
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Instructeur)
class InstructeurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    search_fields = ('nom', 'prenom', 'email')

