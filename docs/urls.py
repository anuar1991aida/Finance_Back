from django.urls import path
from . import views

urlpatterns = [
    path('utvinclist', views.utvinclist, name='index'),
    path('utvincitem/<int:id>', views.utvincitem, name='index'),
    path('utvincsave', views.utvincsave, name='index'),
    path('utvincdelete/<int:id>', views.utvincdelete, name='index'),

    path('izminclist', views.izminclist, name='index'),
    path('izmincitem/<int:id>', views.izmincitem, name='index'),
    path('izmincsave', views.izmincsave, name='index'),
    path('izmincdelete/<int:id>', views.izmincdelete, name='index'),
    path('incgetplanbyclassif', views.incgetplanbyclassif, name='index'), 

    path('import219', views.import219, name='index'), 
]