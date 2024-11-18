from django.urls import path
from django.contrib.auth import views as auth_views     #We renamed the 'views' as 'auth_views' since ther's already 'views'
from . import views

urlpatterns = [
    #Auth URLs
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),        #Does not need any template
    path('signup/', views.signup, name="signup"),   #View was used because it auth_views does not have signup class and you would need to create a view for signup and a template as well.

    path('', views.post_list, name="post_list"),
    path('<int:post_id>/', views.post_detail, name="post_details"),
    #path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # URL for editing a post

    path('create/', views.post_create, name='post_create'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]