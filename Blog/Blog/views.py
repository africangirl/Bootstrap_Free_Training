from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
from .forms import PostForm
from django.core.exceptions import PermissionDenied


def post_list(request):
    posts = Post.objects.all()
    can_add_post = request.user.has_perm("Blog.add_post")
    return render(request, 'Blog/post_list.html', {'posts': posts,"can_add_post":can_add_post})

def listhome(request):
    posts = Post.objects.all()
    return render(request, 'Blog/listhome.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'Blog/post_detail.html', {'post': post})

# @permission_required("myBlog.add_post", raise_exception=True)
@login_required
def post_create(request):
    if not request.user.has_perm("Blog.add_post"):
        raise PermissionDenied
    if request.method =='POST':
       form = PostForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'Blog/post_form.html', {'form':form})  #Get forms

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})








#     # Import necessary functions from Django
# from django.shortcuts import render, get_object_or_404
# # Import the Post model from the current app's models
# from .models import Post

# # Define the view function for displaying a list of posts
# def post_list(request):
#     # Query the database for all Post objects and assign them to 'posts'
#     posts = Post.objects.all()
#     # Render the 'post_list.html' template, passing 'posts' as context
#     return render(request, 'Blog/post_list.html', {'posts': posts})

# # Define the view function for displaying a single post's details
# def post_detail(request, post_id):
#     # Retrieve a single Post object by 'id' or return a 404 error if not found
#     post = get_object_or_404(Post, id=post_id)
#     # Render the 'post_detail.html' template, passing the 'post' as context
#     return render(request, 'Blog/post_detail.html', {'post': post})


# def post_create(request):  # Define a function to handle creating a new post
#     if request.method == 'POST':  # Check if the HTTP request method is POST (indicating form submission)
#         form = PostForm(request.POST)  # Initialize a PostForm instance with submitted form data
#         if form.is_valid():  # Validate the form to ensure all required fields are filled correctly
#             form.save()  # Save the form data to create a new Post instance in the database
#     else:  # If the request method is not POST (e.g., GET request)
#         form = PostForm()  # Initialize an empty PostForm instance for a blank form
#         return render(request, 'Blog/post_form.html', {'form': form})  # Render the form template, passing the form context
