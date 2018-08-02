from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.conf.urls import url

from . import views
urlpatterns=[
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/logout', include('django.contrib.auth.urls')),
	path('accounts/login', include('django.contrib.auth.urls')),
	path('', views.index, name='index'),
	path('Presentation/', views.quisommesnous, name='presentation'),
	path('Organisation/', views.organisation, name='Organisation'),
	path('Contact/', views.contact, name='Contact'),
	path('Galerie/', views.galerie, name='galerie'),
	path('Enseignements/', views.enseignement, name='Enseignements'),
	path('Evenements/', views.evenement, name='evenements'),
	path('Pain quotidien/', views.pain, name='pain'),
	path('Les discussions/', views.discussion, name='discussion'),
	path('Impliquez vous/', views.impliquez_vous, name='implique'),
	path('Don/', views.don, name='don'),
	path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
	url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
	path('signup/', views.signup, name='signup'),
	url(r'^Watch$', views.play, name='play'), 
	url(r'^Pain-details$', views.pain_detail, name='pain_detail'),
	url(r'^comment/$', views.comment, name='comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
