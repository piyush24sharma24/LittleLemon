from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view()
def menu_list(request):
    return Response('List of Menu_items', status=status.HTTP_200_OK)