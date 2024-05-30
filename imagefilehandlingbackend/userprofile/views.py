from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
