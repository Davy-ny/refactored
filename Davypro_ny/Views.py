from django.shortcuts import render

def Aboutpage(request):
    return render(request, 'About.html')

def Homepage(request):
    return render(request, 'Home.html')

def Blogpage(request):
    return render(request, 'Blog.html')

def Contactpage(request):
    return render(request, 'Contact.html')

def Servicespage(request):
    return render(request, 'Services.html')

def Productpage(request):
    return render(request, 'Product.html')

def Indexpage(request):
    return render(request, 'index.html')





