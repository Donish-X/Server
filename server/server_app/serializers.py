from rest_framework import serializers
from .models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Belt, Coaches, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Gruppa, Payments, Sportsmens, Visition

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class BeltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belt
        fields = '__all__'

class CoachesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaches
        fields = '__all__'

class GruppaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gruppa
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class SportsmensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportsmens
        fields = '__all__'

class VisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visition
        fields = '__all__'
