# hotel/urls.py
from django.urls import path
from . import views
from AuthApp import views as v1
from HotelApp import views as v2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('term/',views.term,name='term'),
    path('setting/',views.setting,name='setting'),
    path('help/',views.help,name='help'),
    path('about/',views.about,name='about'),
    # path('amazing/',views.amazing,name='amazing'),
    path('beach/',views.beach,name='beach'),
    path('coming/',views.coming,name='coming'),
    path('confirm/',views.confirm,name='confirm'),
    path('contact/',views.contact,name='contact'),
    path('data/',views.data,name='data'),
    path('homepage/',views.homepage,name='homepage'),
    path('luxury/',views.luxury,name='luxury'),
    path('learn/',views.learn,name='learn'),
    path('rooms/',views.rooms,name='rooms'),
    path('search/',views.search,name='search'),
    path('feedback/',views.help,name='feedback'),
    path('AuthApp/login/',v1.login_view,name='login'),
    path('AuthApp/register/',v1.register_view,name='register'),
    path('AuthApp/logout/', v1.logout_view, name='logout'),
    path('AuthApp/profile/', v1.view_profile, name='view_profile'),
    

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)