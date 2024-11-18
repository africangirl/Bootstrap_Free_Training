from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),


    path('', views.post_list, name="post_list"),
    path('listhome/', views.listhome, name="listhome"),
    path('<int:post_id>/', views.post_detail, name="post_details"),
    path('create/',views.post_create, name="post_create" ),
]



# # Import the `path` function from Django's URL module and the `views` module from the current directory
# from django.urls import path
# from . import views

# # Define URL patterns for the application
# urlpatterns = [
#     # This line maps the root URL ('') to the `post_list` view function in `views`
#     # The URL name 'post_list' can be used in templates or other parts of the app to refer to this path
#     path('', views.post_list, name="post_list"),
    
#     # This line maps URLs containing an integer (`<int:post_id>/`) to the `post_detail` view function
#     # `<int:post_id>` is a path converter that captures the integer part of the URL and passes it as the `post_id` argument to `post_detail`
#     # The URL name 'post_details' can be used to refer to this path in templates and view functions
#     path('<int:post_id>/', views.post_detail, name="post_details"),
#     # This line creates a dynamic URL where <int:post_id> captures a specific post’s ID as an integer.
# ]
