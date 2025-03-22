
from django.contrib.auth import authenticate  
from rest_framework import generics, status  
from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework.permissions import IsAuthenticated  
from rest_framework.authtoken.models import Token  
from .models import Book  
from .serializers import AdminSignupSerializer, AdminLoginSerializer, BookSerializer  


class AdminSignupView(generics.CreateAPIView):  
    serializer_class = AdminSignupSerializer  

class AdminLoginView(APIView):  
    def post(self, request):  
        serializer = AdminLoginSerializer(data=request.data)  
        if serializer.is_valid():  
            username = serializer.validated_data['username']  
            password = serializer.validated_data['password']  
            user = authenticate(username=username, password=password)  
            if user:  
                token, created = Token.objects.get_or_create(user=user)  
                return Response({'token': token.key})  
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)  


class BookListCreateView(generics.ListCreateAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]  
  
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [IsAuthenticated]
