from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .forms import PostForm,ProfileForm
from .models import Post,Profile
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied



def post_list(request):
    posts = Post.objects.all()   #Get all the object
    can_add_post = request.user.has_perm("myBlog.add_post")
    return render(request, 'myBlog/post_list.html', {'posts': posts, 'can_add_post':can_add_post})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'myBlog/post_detail.html', {'post':post})


 
@login_required
# @permission_required("myBlog.add_post", raise_exception=True)  #you can use this instead of using the if statement that contains the PermissionDenied 
def post_create(request):
    if not request.user.has_perm('myBlog.add_post'):        #Checks if user has permission to add post
        raise PermissionDenied      #Raises an exception if the user doesn't have the perm to add post
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)     #When saved it will not go straight into the database and it as a
            post.author = request.user      #Assigns the currently logged-in user as the author of the post.
            post.save() #Saves the post to the db
            return redirect('post_list')
    else:
        form = PostForm()   
        return render(request,"myBlog/post_form.html", {'form':form})

# def post_edit(request, post_id):
#     post = get_object_or_404(Post, id=post_id)  # Get the existing post
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)  # Bind the form to the existing post
#         if form.is_valid():
#             form.save()  # Update the post
#             return redirect('post_list')  # Redirect to the list of posts after saving
#     else:
#         form = PostForm(instance=post)  # Create a form with the existing post's data

#     return render(request, 'myBlog/post_form.html', {'form': form, 'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)    #Usercreation form creates the form for the signup
        if form.is_valid():    #CHecks if the signup from is valid
            user = form.save() #Returns the user after saving,register the user 
            login(request, user)  #Login the user after registering/verifying the user
            return redirect('post_list')  #Redirect the user after login
    else:
        form = UserCreationForm()   #Creates the form

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'myBlog/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.Profile)    #Gets the form from the saved filed file from the instances of what we are updating
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'myBlog/edit_profile.html' ,{'form':form})




# ALTERNATIVE
#from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
# from .forms import PostForm
# from .models import Post

# def post_list(request):
#     posts = Post.objects.all()  # Get all the posts
#     return render(request, 'myBlog/post_list.html', {'posts': posts})

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, 'myBlog/post_detail.html', {'post': post})

# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():  # Use is_valid() to check if the form is valid
#             form.save()  # Call save() to save the form data to the database
#             return redirect('post_list')  # Redirect to the post list after saving
#     else:
#         form = PostForm()  # Create an empty form if the request is not POST

#     return render(request, "myBlog/post_form.html", {'form': form})  # Pass the form to the template
