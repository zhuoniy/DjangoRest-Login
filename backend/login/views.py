from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets

User = get_user_model()

class loginView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')

