from django.shortcuts import render,HttpResponse,redirect
import requests
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from newsapi import NewsApiClient   

def home(request):
   url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=56cee1298f47499591eed44b38f9db5f"
    
   query = request.GET.get('query', '')
   response = requests.get(url)
   news_api = response.json()
    
   articles = news_api.get("articles", [])
    
   context = {'articles': articles,'query':query}
   return render(request, 'home.html',context) 

def content(request):
    return render(request, 'content.html', {'content': content})

def search(request): 
    articles = []
    query = request.GET.get('query') 
    if query:  
        api_key = '56cee1298f47499591eed44b38f9db5f'
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
        response = requests.get(url)
        data = response.json()
        
        articles = data.get('articles', [])  

   

    return render(request,'search.html', {'articles': articles, 'query': query})


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        Confirmpassword = request.POST['Confirmpassword']
        email = request.POST['email']
        phone = request.POST['phone'] 
        
        
        if len(name)>10:
            messages.error(request,"username must be under 10 Characters..")
            return redirect('home')
        
        if not name.isalnum():
            messages.error(request, "username should only contains letters and numberes")
            return redirect('home')
        
        if password != Confirmpassword:
            messages.error(request, "password did not match!")
            return redirect('home')
        
        myuser = User.objects.create_user(name, email, password)
        myuser.name = name
        myuser.save()
        messages.success(request,"your account was created successfully!")
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")    
    
def handlelogin(request):
    if request.method == "POST":
        loginname = request.POST['loginname']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginname, password=loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, "User Login Succesfully!")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials")
            return redirect('home')
    return HttpResponse('404 - Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request, "successfully Logout!!")
    return redirect('home')
    return HttpResponse('handlelogout')


