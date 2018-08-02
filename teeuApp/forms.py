from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Entrer une adresse mail valid svp.')
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ContactForm(forms.Form):
	"""docstring for ContactForm"""
	email = forms.EmailField(max_length=254, help_text='babagod@site.com', required=True)
	first_name = forms.CharField(label='Nom' ,max_length=30, required=True)
	last_name = forms.CharField(label='Prenom',max_length=30, required=True)
	pays = forms.CharField(label='Pays',max_length=15, required=False)
	ville = forms.CharField(label = 'Ville',max_length=15, required=False)
	phone = forms.CharField(label ='Telephone',max_length=15, required=False)
	subject = forms.CharField(label ='Sujet',max_length=100, required=True)
	request = forms.CharField(label='Demande/Question',widget=forms.Textarea)


class PainCommentForm(forms.Form):
	"""docstring for Pain_commentForm"""
	comment = forms.CharField(label='Demande/Question',widget=forms.Textarea)
	

class PainReplyForm(forms.Form):
	"""docstring for PainReplyForm"""
	reply = forms.CharField(label='Demande/Question',widget=forms.Textarea)

