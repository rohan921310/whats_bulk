from django.shortcuts import render,redirect
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from send.unsaved_contacts import whatsapp_login

def home_view(request):
    return render(request,"home.html")