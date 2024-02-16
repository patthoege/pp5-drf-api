from rest_framework.decorators import api_view
from rest_framework.response import Response


# Code provided in DRF-API walkthrough.
@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my PP5 Django Rest Framework API!"
    })