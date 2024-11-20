from django.urls  import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
   
]


# path('sample/', views.sample, name='sample'),
# path('login/', views.login_view, name='login'),
# path('dashboard/', views.dashboard_view, name='dashboard')