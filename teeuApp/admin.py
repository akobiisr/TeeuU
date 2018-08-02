from django.contrib import admin

# Register your models here.
from teeuApp.models import *
#class AffichageDeVersetAdmin(admin.ModelAdmin):
	#"""docstring for AffichageDeVersetAdmin"""
	#list_display = ('id', 'verset', 'date','date_mod')
class EnseignementAdmin(admin.ModelAdmin):
	"""docstring for VersetDuJourAdmin"""
	list_display = ('id', 'titre', 'predicateur','predication','date_pred','date_enreg','date_modif')

class VersetDuJourAdmin(admin.ModelAdmin):
	"""docstring for VersetDuJourAdmin"""
	list_display = ('id', 'verset','date_pub','date_mod','jourDePub')

class ImageThemeAdmin(admin.ModelAdmin):
	"""docstring for VersetDuJourAdmin"""
	list_display = ('id', 'theme', 'description','date_pub','date_mod')

class EvenementAdmin(admin.ModelAdmin):
	"""docstring for QuiSommeNousAdmin"""
	list_display = ('id', 'date_even', 'titre','date_fin')
		
	

#admin.site.register(AffichageDeVerset, AffichageDeVersetAdmin)

admin.site.register(VersetDuJour, VersetDuJourAdmin)

admin.site.register(ImageTheme, ImageThemeAdmin)

admin.site.register(Evenement,EvenementAdmin)
admin.site.register(Enseignement,EnseignementAdmin)
admin.site.register(Galerie)
admin.site.register(Pain_Quotidien)



