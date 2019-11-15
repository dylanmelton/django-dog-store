from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html", {"dog_products": dog_products})

def dog_product_detail(request, id):
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})

def purchase_dog_product(request):
    pass

def purchase_detail(request):
    pass

def new_dog_tag(request):
    pass

def dog_tag_list(request):
    pass