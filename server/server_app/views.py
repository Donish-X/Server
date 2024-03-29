from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AuthSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import UsersData
import json


from .models import Sportsmens, Visition
from .serializers import SportsmensSerializer, VisitionSerializer

from .models import Sportsmens, Gruppa
from .serializers import SportsmensSerializer, GruppaSerializer



class RegisterUserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            # Получаем данные из POST-запроса
            data = request.data

            # Получаем логин и пароль из данных
            login = data.get('login')
            password = data.get('password')

            # Проверяем, существует ли пользователь с таким логином
            if UsersData.objects.filter(login=login).exists():
                return JsonResponse({'status': 'error', 'message': 'Пользователь с таким логином уже существует'})

            # Создаем нового пользователя
            UsersData.objects.create(login=login, password=password)

            return JsonResponse({'status': 'success', 'message': 'Регистрация прошла успешно'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

class SportsmensList(generics.ListCreateAPIView):
    queryset = Sportsmens.objects.all()
    serializer_class = SportsmensSerializer

    def get(self, request, *args, **kwargs):
        # Обработка GET запроса
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Обработка POST запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GroupList(generics.ListCreateAPIView):
    queryset = Gruppa.objects.all()
    serializer_class = GruppaSerializer

    def get(self, request, *args, **kwargs):
        # Обработка GET запроса
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Обработка POST запроса
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class SportsmensByGroupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Обработка POST-запроса
        group_id = request.data.get('group')  
        
        if group_id is not None:
            sportsmens = Sportsmens.objects.filter(gruppa=group_id)
            serializer = SportsmensSerializer(sportsmens, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing group_id in the request'}, status=status.HTTP_400_BAD_REQUEST)
        

  



class SportsmenDetailsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Получение данных из запроса Android
        sportsmen_name = request.data.get('name')
        visit_date = request.data.get('date')

        if sportsmen_name is not None and visit_date is not None:
            # Создание новой записи Sportsmens
            # sportsmen_data = {'name': sportsmen_name}
            # sportsmen_serializer = SportsmensSerializer(data=sportsmen_data)
            # if sportsmen_serializer.is_valid():
            #     sportsmen_serializer.save()
            # else:
            #     return Response({'error': 'Invalid data for Sportsmen'}, status=status.HTTP_400_BAD_REQUEST)

            # Создание новой записи Visition
            visit_data = {'name': sportsmen_name, 'visit': visit_date}
            visit_serializer = VisitionSerializer(data=visit_data)
            if visit_serializer.is_valid():
                visit_serializer.save()
            else:
                # Если данные для Visition неверны, удаляем созданную запись Sportsmens
                Sportsmens.objects.get(name=sportsmen_name).delete()
                return Response({'error': 'Invalid data for Visition'}, status=status.HTTP_400_BAD_REQUEST)

            # Возврат данных в ответе
            return Response({
                # 'sportsmen': sportsmen_serializer.data,
                'visit': visit_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Missing name or date in the request'}, status=status.HTTP_400_BAD_REQUEST)


class AuthView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Просто возвращаем данные для теста
        return Response({'message': 'GET запрос для аутентификации', 'status': 'success'}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
