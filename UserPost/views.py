from django.shortcuts import render

# Create your views here.
from .models import User, Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def dashboard(request):
    return render(request,'UserPost/dashboard.html',{'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
        return render(request,'UserPost/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'UserPost/register.html',{'user_form': user_form})

@login_required
def newpost(request, username):
    if request.method == 'POST':
        user = get_object_or_404(User, username=username)
        textarea = request.POST["textarea"]
        if not textarea:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        post = Post.objects.create(text=textarea, user=user)
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
