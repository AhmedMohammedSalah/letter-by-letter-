from django.urls import path
from .views import login_view ,signup_view,logout_view
app_name='accounts'
urlpatterns = [
    # account main 
    # path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'), 
    # path('',home,name='login_home' ),
    # Profile 
    
]