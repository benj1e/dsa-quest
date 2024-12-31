from django.shortcuts import render, redirect
from django.http import HttpRequest


# Create your views here.
def landing_page(request: HttpRequest):
    """Landing page view"""
    return render(request, "app/landing_page.html")


def question(request: HttpRequest):
    """DSA Journey: Questions view"""
    return render(request, "app/question.html")
