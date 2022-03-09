from genericpath import exists
from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Food, Category, Source, List


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "list/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "list/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "list/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "list/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "list/register.html")

def index(request):
    if request.user.is_authenticated:
        active_user = User.objects.get(username=request.user)
        # if no foods in user's list, return all foods ordered by name
        if List.objects.filter(user=active_user).count() == 0:
            foods = Food.objects.all().order_by("name")
        else:
            # get list of food in user's list
            to_exclude = List.objects.get(user=active_user)
            # filter out foods in list and return foods
            foods = Food.objects.exclude(id__in=to_exclude.foods.all()).order_by("name")
    else:
        foods = Food.objects.all().order_by("name")
    
    categories = Category.objects.all()
    sources = Source.objects.all()
    category_name = ""

    if request.GET.get("filter"):
        category_id = request.GET.get("filter")
        if category_id == "all":
            return HttpResponseRedirect(reverse("index"))
        else:
            category_name = Category.objects.get(id=category_id).name
            foods = Food.objects.filter(category=category_id).order_by("name")
    
    paginator = Paginator(foods, 12)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    return render(request, "list/index.html", {
        "foods": page_obj,
        "foods_count": foods.count(),
        "categories": categories,
        "category": category_name,
        "sources": sources,
    })

def list(request):
    active_user = User.objects.get(username=request.user)

    if List.objects.filter(user=active_user).count() == 0:
        list = List(user=active_user)
        list.save()
    else:
        list = List.objects.get(user=active_user)
        
    foods = list.foods.all().order_by("name")

    paginator = Paginator(foods, 20)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    return render(request, "list/list.html", {
        "foods": page_obj,
        "foods_count": foods.count(),
    })

def add(request, id):
    try:
        food = Food.objects.get(id=id)
        list = List.objects.get(user=request.user)
        if food not in list.foods.all():
            list.foods.add(food)
            return JsonResponse({
                "message": "Added!",
                "count": list.foods.count(),
            })
        else:
            list.foods.remove(food)
            return JsonResponse({
                "message": "Removed!",
                "count": list.foods.count(),
            })
    except Food.DoesNotExist:
        return JsonResponse({
            "message": "Food does not exist.",
        })
