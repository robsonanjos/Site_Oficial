from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gemas', views.gemas, name='gemas'),
    path('historia', views.historia, name='historia'),
    path('contato', views.contato, name='contato'),
    path('download', views.download, name='download'),
    path('equipe', views.equipe, name='equipe'),
    path('faq', views.faq, name='faq'),
    path('mapas', views.mapas, name='mapas'),
    path('personagens', views.personagens, name='personagens'),
    path('politica-de-privacidade', views.politica, name='politica-de-privacidade'),
    path('agradecimento', views.agradecimento, name='agradecimento'),
    path('Season_Gems.zip', views.download_file),

]
