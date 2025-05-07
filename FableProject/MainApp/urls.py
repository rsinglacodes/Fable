# hotel/urls.py
from django.urls import path
from . import views
from AuthApp import views as v1
from HotelApp import views as v2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('term/', views.term, name='term'),
    path('setting/', views.setting, name='setting'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('beach/', views.beach, name='beach'),
    path('coming/', views.coming, name='coming'),
    path('confirm/', views.confirm, name='confirm'),
    path('contact/', views.contact, name='contact'),
    path('data/', views.data, name='data'),
    path('homepage/', views.homepage, name='homepage'),
    path('luxury/', views.luxury, name='luxury'),
    path('learn/', views.learn, name='learn'),
    path('rooms/', views.rooms, name='rooms'),
    path('search/', views.search, name='search'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('cost-estimator/', views.cost_estimator, name='cost_estimator'),
    path('api/trip-cost-estimate/', views.trip_cost_estimate_api, name='trip_cost_estimate_api'),
    path('api/generate-invoice/', views.generate_invoice, name='generate_invoice'),
    path('AuthApp/login/', v1.login_view, name='login'),
    path('AuthApp/register/', v1.register_view, name='register'),
    path('AuthApp/profile/', v1.view_profile, name='profile'),
    path('AuthApp/logout/', v1.logout_view, name='logout'),
    path('AuthApp/profile/', v1.view_profile, name='view_profile'),
    path('thanks/<str:sentiment>/', views.thanks, name='thanks'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)