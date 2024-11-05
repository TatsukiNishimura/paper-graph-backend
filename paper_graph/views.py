from django.shortcuts import render
from rest_framework import viewsets

from .models import Paper
from .serializers import PaperSerializer


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

    def partial_update(self, request, *args, **kwargs):
        print(request.data)
        return super().partial_update(request, *args, **kwargs)
