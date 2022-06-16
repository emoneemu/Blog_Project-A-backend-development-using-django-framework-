from django.urls import path
from Login_App import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
app_name = 'Login_App'

urlpatterns = [
    path('signup/',views.sign_up,name="signup"),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change-profile/',views.user_change,name='user_change'),
    path('password/',views.pass_change,name='pass_change'),
    path('add-picture/',views.add_pro_pic,name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic,name='change_pro_pic')
]
