from rest_framework.response import Response
from rest_framework import generics, status
from foodharbor.models import StoreCategory
from foodharbor.serializers import StoreCategorySerializer

class StoreCategoryView(generics.CreateAPIView):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StoreCategoryListView(generics.ListAPIView):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer