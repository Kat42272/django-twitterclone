from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView, View

from .forms import LoginForm

# Matt Perry helped me work out the bugs with my function to class errors


# Create your views here.


# def login_view(request):
#   if request.method == 'POST':
#     form = LoginForm(request.POST)
#     if form.is_valid():
#       data = form.cleaned_data
#       user = authenticate(
#         request,
#         username=data.get('username'),
#         password=data.get('password'),
#       )
#       if user:
#         login(request, user)
#         return HttpResponseRedirect(reverse('homepage'))
#   form = LoginForm()
#   return render(
#     request,
#     'login.html',
#     {'form': form},
#   )

class LoginView(TemplateView):

  def get(self, request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    # form = LoginForm(request.POST)
    if user is not None:
      if user.is_active:
        login(request, user)

        return HttpResponseRedirect('/')
      else:
        return HttpResponse('Inactive user.')


      # data = form.cleaned_data
      # user = authenticate(
      #   request,
      #   username=data.get('username'),
      #   password=data.get('password'),
      # ) 
      # breakpoint()
      # if user:
      #   login(request, user)
        return HttpResponseRedirect(reverse('homepage'))
    # else:
    #   return render(request, 'login.html', {'form': form})


# def logout_view(request):
#   logout(request)
#   return HttpResponseRedirect(reverse('homepage'))

class LogoutView(View):
  def get (self, request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))