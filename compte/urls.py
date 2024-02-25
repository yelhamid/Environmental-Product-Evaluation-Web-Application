from django.urls import path
from . import views
import pandas as pd
from django.contrib.auth import authenticate

urlpatterns = [ 
    
    path('calcule_sur/matiere',views.matiere,name='matiere'),
    path('calcule_sur/procedes',views.procedes,name='procedes'),
    path('calcule_sur/transport',views.transport,name='transport'),
    path('calcule_sur/energie',views.energie,name='energie'),
    path('calcule_sur/fin_vie',views.fin_vie,name='fin_vie'),
    path('recap',views.recap,name='recap'),
    path('utiliser',views.utiliser,name='utiliser'),
    path('inscription',views.inscriptionPage,name='inscription'),
    path('acces',views.accesPage,name='acces'),
    path('logout',views.logOut,name='logout'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),


]
