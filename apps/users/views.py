from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout,authenticate
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
