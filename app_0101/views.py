from django.shortcuts import render, get_object_or_404
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes


def home(request):
    return render(request, '0101_homepage.html', {})

def notes(request):
    return render(request, '0101_django_notes.html', {})

def notes2(request):
    return render(request, '0103_django_serializations.html', {})

# 0103 added method and if else
@api_view(['GET','POST'])
def menu_items(request):
    if(request.method=='GET'):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        if category_name:
            items = items.filter(category__title=category_name)

        # price__lte  aka less than equal to
        if to_price:
            items = items.filter(price__lte=to_price)

        if search:
            items = items.filter(title__contains=search)

        # ex2 title__startswith
        #if search:
        #    items = items.filter(title__startswith=search)

        if search:
            items = items.filter(title__contains=search)
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method=='POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)



