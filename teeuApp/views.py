from django.shortcuts import render
from django.http import HttpResponse
#from .models import AffichageDeVerset
from django.template import loader
from .models import *
import datetime
from django.utils.encoding import force_text
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .forms import *
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.signing import Signer
from django.core import signing
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
now = datetime.datetime.now()
 #Create your views here.
def index(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S"))[:1]

	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()

	if evenement:
		id_first_event = evenement[0].id
	else:
		id_first_event = 0

	next_event1 = Evenement.objects.order_by('date_even').filter(date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S"))

	next_event = next_event1.exclude(id = 0)[:3]

	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()


	predication = Enseignement.objects.order_by('-id')[:1]
	id2 = predication[0].id


	predication1 =Enseignement.objects.order_by('-id').all()
	predication2 =predication1.exclude(id=id2)[:3]
	
	signer = Signer('bV88T')
	signer = Signer(salt='WpzT')
	for i in predication:
		predication[0].id = signer.sign(predication[0].id)

	for pred in predication2:
		pred.id = signer.sign(pred.id)

	template = loader.get_template('teeuApp/index.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        'predication':predication,
        'predication2':predication2,
        'list_event':next_event,
    }
	return HttpResponse(template.render(context, request))

def quisommesnous(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	next_event1 = Evenement.objects.order_by('date_even')[:3]
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()


	template = loader.get_template('teeuApp/presentation.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        #'histoire':histoire,
       # 'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))


def organisation(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()


	template = loader.get_template('teeuApp/organisation.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
       # 'histoire':histoire,
       # 'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))

def contact(request):
	

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			ville = form.cleaned_data['ville']
			pays = form.cleaned_data['pays']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['request']
			phone = form.cleaned_data['phone']
			recipient =['akobiisrael62@gmail.com']

			send_mail(subject,message,email,recipient)

		return redirect('index')

	else:

		theme = ImageTheme.objects.all()
		versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
		evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
		form = ContactForm()
		template = loader.get_template('teeuApp/contact.html')
		context = {
			'evenement':evenement,
        	'versetDuJour':versetDuJour,
        	'theme':theme,
        	'form': form
    	}
		return HttpResponse(template.render(context, request))


def galerie(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	Imagelist = Galerie.objects.order_by('-date_enreg').all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()


	page = request.GET.get('page',1)
	paginator = Paginator(Imagelist,9)
	try:
		ImageGalerie = paginator.page(page)
	except PageNotAnInteger:
		ImageGalerie = paginator.page(1)
	except EmptyPage:
		ImageGalerie = paginator.page(paginator.num_pages)

	
	template = loader.get_template('teeuApp/galerie.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        'galerie':ImageGalerie,
        #'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))


def enseignement(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()

	enseignement_list =Enseignement.objects.order_by('-id').all()
	
	signer = Signer('bV88T')
	signer = Signer(salt='WpzT')
	

	for pred in enseignement_list:
		pred.id = signer.sign(pred.id)

	page = request.GET.get('page',1)
	paginator = Paginator(enseignement_list,9)
	try:
		predications = paginator.page(page)
	except PageNotAnInteger:
		predications = paginator.page(1)
	except EmptyPage:
		predications = paginator.page(paginator.num_pages)


	template = loader.get_template('teeuApp/enseignement.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        'predications':predications,
        #'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))


def play(request):
	#recuperer l'id envoyer dans l'url
	query = request.GET.get('id')
	#decryper l'id
	signer = Signer('bV88T')
	signer = Signer(salt='WpzT')
	try:
		value = signer.unsign(query)
	except (signing.BadSignature, TypeError, ValueError, OverflowError):
		return redirect('Enseignements')
	
	#selection de l'enseignement apres avoir decrypter l'id
	predication =Enseignement.objects.filter(id=value)
	for i in predication:
		genre_de_predication = i.genre

	#selection des enseignement du meme genre
	predication_list = Enseignement.objects.order_by('-id').exclude(id=value).filter(genre=genre_de_predication)

	#crypter les id des enseignements selectionnee
	for predecat in predication_list:
		predecat.id = signer.sign(predecat.id)

	#selection des autres 
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	theme = ImageTheme.objects.all()

	

	

	page = request.GET.get('page',1)
	paginator = Paginator(predication_list,3)
	try:
		predications = paginator.page(page)
	except PageNotAnInteger:
		predications = paginator.page(1)
	except EmptyPage:
		predications = paginator.page(paginator.num_pages)

	template = loader.get_template('teeuApp/play.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        'predication':predication,
        'predications':predications,
    }
	return HttpResponse(template.render(context, request))

def evenement(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()


	template = loader.get_template('teeuApp/evenement.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        #'histoire':histoire,
        #'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))

def pain(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	pain_quotidient_list = Pain_Quotidien.objects.order_by('-date_enreg')
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()

	signer = Signer('bV88T')
	signer = Signer(salt='WpzT')
	

	for pain in pain_quotidient_list:
		pain.id = signer.sign(pain.id)


	page = request.GET.get('page',1)
	paginator = Paginator(pain_quotidient_list,5)
	try:
		pain_quotidient = paginator.page(page)
	except PageNotAnInteger:
		pain_quotidient = paginator.page(1)
	except EmptyPage:
		pain_quotidient = paginator.page(paginator.num_pages)


	template = loader.get_template('teeuApp/pain.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        'pain_quotidient':pain_quotidient,
        #'vision':vision,
       # 'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))


def discussion(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	
	template = loader.get_template('teeuApp/discussion.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
    }
	return HttpResponse(template.render(context, request))


def impliquez_vous(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()


	template = loader.get_template('teeuApp/implique.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        #'histoire':histoire,
        #'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))


def don(request):
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()


	template = loader.get_template('teeuApp/implique.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        #'histoire':histoire,
        #'vision':vision,
        #'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))




#def test(request, id):
	
#	histoire = Presentation.objects.filter(id=id).values()
	

#	template = loader.get_template('teeuApp/test.html')
#	context = {
        
  #      'histoire':histoire,
       
  #  }
#	return HttpResponse(template.render(context, request))





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('teeuApp/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'teeuApp/signup.html', {'form': form})

def account_activation_sent(request):
	return render(request, 'teeuApp/confirm.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'teeuApp/account_activation_invalid.html')


def pain_detail(request):

	#recuperer l'id envoyer dans l'url
	query = request.GET.get('id')
	#decryper l'id
	signer = Signer('bV88T')
	signer = Signer(salt='WpzT')
	try:
		value = signer.unsign(query)
	except (signing.BadSignature, TypeError, ValueError, OverflowError):
		return redirect('pain')
	
	#selection de le pain apres avoir decrypter l'id
	pain =Pain_Quotidien.objects.filter(id=value)

	

	#selection des 3 derniers pains
	pain_list = Pain_Quotidien.objects.order_by('-date_enreg').exclude(id=value)[:3]#.filter(date_enreg__lt=date_enreg_pain)[:3]

	#comment_user = Commentaire_pain.objects.filter(User__id =1)
	comment_user = Commentaire_pain.objects.filter(id_pain=value)

	#crypter les id des enseignements selectionnee
	for predecat in pain_list:
		predecat.id = signer.sign(predecat.id)
	#evenement = Evenement.objects.filter( date_even ='2018-03-14 13:32:04').values()
	evenement = Evenement.objects.order_by('date_even').filter( date_even__gt =now.strftime("%Y-%m-%d %H:%M:%S")).values()[:1]
	versetDuJour = VersetDuJour.objects.filter(jourDePub = now.strftime("%Y-%m-%d")).values()
	#versetDuJour = VersetDuJour.objects.order_by('id')[:1]
	theme = ImageTheme.objects.all()
	#histoire = Presentation.objects.filter(titre='Notre Histoire').values()
	#vision = Presentation.objects.filter(titre='Notre Vision').values()
	#objectif = Presentation.objects.filter(titre='Notre Objectif').values()
	FormReply =PainReplyForm()
	FormComment=PainCommentForm()



	template = loader.get_template('teeuApp/pain-details.html')
	context = {
		'evenement':evenement,
        'versetDuJour':versetDuJour,
        'theme':theme,
        'pain_detail':pain,
        'pain_quotidient':pain_list,
        'reply': FormReply,
        'comment':FormComment,
        'commentaire':comment,
        'liste_comment_user':comment_user,

       # 'objectif':objectif,
    }
	return HttpResponse(template.render(context, request))

def comment(request):

	if request.method == 'GET':
		id_pain = request.GET.get('pain')
		id_user = request.GET.get('user')
		comment = request.GET.get("commentaire")
		data ={}

		pain =  get_object_or_404(Pain_Quotidien, id=id_pain)
		user = get_object_or_404(User, id=id_user)
		commentaire = Commentaire_pain.objects.create(
					id_pain = pain,
					Commentaire = comment,
					user = user
					)
		data ={
		'objet':id_pain
		}

	return JsonResponse(data)
