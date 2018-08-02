from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    photo_profil = models.ImageField("Photo de profil", null=True)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class VersetDuJour(models.Model):
	"""docstring for VersetDuJour"""
	verset = models.CharField("Verset", max_length=50)
	textDuVerset = models.TextField("Text du verset", max_length=500)
	jourDePub = models.DateField("Verset du jour",null=True)
	date_pub = models.DateTimeField("Date", auto_now_add=True)
	date_mod = models.DateTimeField("Date de Modification", auto_now=True)
	def __str__(self):
		return self.verset

class ImageTheme(models.Model):
	"""docstring for ImageTheme"""
	description = models.TextField("Description", max_length=500)
	theme = models.ImageField(upload_to='teeuApp/theme')
	date_pub = models.DateTimeField("Date", auto_now_add=True)
	date_mod = models.DateTimeField("Date de Modification", auto_now=True)
	def __str__(self):
		return self.description

class Enseignement(models.Model):
	GENRE_TYPE=(
		('video', 'Video'),
		('Audio', 'Audio'),
		)
	PRED_TYPE = (
		('Pasteur', 'Pasteur'),
		('Ancien', 'Ancien'),
		('Frère','Frère'),
		('Madame','Madame'),
		('Rev.','Rev.'),
		('Apotre','Apotre'),
		('Autre','Predicateur'),
		)
	"""docstring for video"""
	titre = models.CharField("Titre", max_length=50)
	Titre_predicateur = models.CharField("Titre du predicateur",max_length=15,choices=PRED_TYPE)
	predicateur = models.CharField("Predicateur", max_length=50)
	date_pred = models.DateTimeField("Date de la predication")
	date_enreg = models.DateTimeField("Date de Publication", auto_now_add=True)
	date_modif =models.DateTimeField("Date de derniere Modification", auto_now=True)
	genre = models.CharField("Genre",max_length=10,choices=GENRE_TYPE)
	image_dispaly = models.ImageField("Image de couverture",upload_to='teeuApp/Enseignement/cover',help_text="SVP, une image respectant les dimensions 263x177.")
	predication = models.FileField(upload_to='teeuApp/Enseignement/fichier', max_length=200)
	
	def __str__(self):
		return self.titre
	


class Evenement(models.Model):
	"""docstring for Evenement"""
	titre = models.CharField("Titre", max_length=50)
	image = models.ImageField("Image de l'Evenement",help_text="SVP, une image respectant les dimensions 263x177.",upload_to='teeuApp/Evenement')
	date_even = models.DateTimeField("Jour de l'evenement")
	lieu = models.CharField("Lieu de l'Evenement", max_length=50)
	date_fin =models.DateTimeField("Date de fin de l'evenement")
	#heure_fin = models.TimeField("A (Heure)")
	resume = models.TextField("Resume de l'Evenement")
	Information_supplementaire =models.TextField("Information supplementaire")
	date_enreg = models.DateTimeField("Date de Publication", auto_now_add=True)
	date_modif =models.DateTimeField("Date de derniere Modification", auto_now=True)
	
	def __str__(self):
		return self.titre


class Galerie(models.Model):
	"""docstring for Evenement"""
	#titre = models.CharField("Titre", max_length=50)
	#thumbnailImage = models.ImageField("Image d'affichage",help_text="SVP, une image respectant les dimensions 500x335.",upload_to='teeuApp/Galerie/thumbnail')
	Image = models.ImageField("Image en taille",upload_to='teeuApp/Galerie/Image')
	Commentaire = models.TextField("Info", null=True)
	date_enreg = models.DateTimeField("Date de Publication", auto_now_add=True)
	date_modif =models.DateTimeField("Date de derniere Modification", auto_now=True)
	
	def __str__(self):
		return 'Image'
		
class Pain_Quotidien(models.Model):
	PRED_TYPE = (
		('Pasteur', 'Pasteur'),
		('Ancien', 'Ancien'),
		('Frère','Frère'),
		('Madame','Madame'),
		('Rev.','Rev.'),
		('Apotre','Apotre'),
		('Autre','Predicateur'),
		)
	titre = models.CharField("Titre", max_length=50)
	Text_de_base = models.CharField("Text de base", max_length=100)
	titre_posteur = models.CharField("Titre du posteur",max_length=15,choices=PRED_TYPE)
	nom = models.CharField("Nom du posteur", max_length=100)
	date_enreg = models.DateTimeField("Date de Publication", auto_now_add=True)
	date_modif =models.DateTimeField("Date de derniere Modification", auto_now=True)
	image_dispaly = models.ImageField("Image de couverture",upload_to='teeuApp/Pain',help_text="SVP, une image respectant les dimensions 263x177.")
	Text = models.TextField("Message")

	"""docstring for Pain_Quotidien"""
	def __str__(self):
		return self.titre

class Commentaire_pain(models.Model):
	"""docstring for Commentaire_pain"""
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	id_pain = models.ForeignKey(Pain_Quotidien, on_delete=models.DO_NOTHING)
	Commentaire = models.TextField("Commentaire")
	date_commentaire = models.DateTimeField("Date", auto_now_add=True)
	def __str__(self):
		return self.id
	
class Reply_pain(models.Model):
	"""docstring for Reply_pain"""
	id_comment = models.ForeignKey(Commentaire_pain, on_delete=models.DO_NOTHING)
	reply = models.TextField("Reply")
	def __str__(self):
		return self.id
		
		