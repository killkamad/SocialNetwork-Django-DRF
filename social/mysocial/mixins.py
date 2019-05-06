from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.shortcuts import redirect
from . import views
from .serializers import FanSerializer

class LikedMixin:
    @detail_route(methods=['POST'])
    def like(self, request, pk=None):

        obj = self.get_object()
        views.add_like(obj, request.user)
        return redirect('com_list')
    @detail_route(methods=['POST'])
    def unlike(self, request, pk=None):

        obj = self.get_object()
        views.remove_like(obj, request.user)
        return redirect('com_list')
    @detail_route(methods=['GET'])
    def fans(self, request, pk=None):

        obj = self.get_object()
        fans = views.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)