from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from foodharbor.models import Store
from foodharbor.serializers import StoreSerializer

class StoreView(generics.CreateAPIView):
    queryset = Store.objects.all().order_by('-created_at')
    serializer_class = StoreSerializer
    permission_classes = [AllowAny]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user

        if user.user_role != 'store':
            return Response({"Message:": "Permission failed. Must be an owner to create a store"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all().order_by('-fantasy_name')
    serializer_class = StoreSerializer