from django.shortcuts import render, redirect
from django.http import HttpRequest


# Create your views here.
def landing_page(request: HttpRequest):
    """Landing page view"""
    return render(request, "app/landing_page.html")


def problem_list(request: HttpRequest):
    """DSA Journey: problem_lists view"""
    return render(request, "app/problem_list.html")


def problem_detail(request: HttpRequest):
    """DSA Journey: problem_list details view"""
    return render(request, "app/problem-details.html")
