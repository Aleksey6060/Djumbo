from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    return render(request, 'categories.html')

def all_products(request):
    return render(request, 'all_products.html')

def cart(request):
    return render(request, 'cart.html')