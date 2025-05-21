from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db.models import Q
from datetime import timedelta

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        usuario = Usuario(**validated_data)
        if password:
            usuario.set_password(password)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

    def validate(self, data):
        data_inicio = data.get('data_inicio')
        data_termino = data.get('data_termino')
        periodo = data.get('periodo')
        sala = data.get('sala_reservada')

        if data_inicio > data_termino:
            raise serializers.ValidationError("A data de início não pode ser posterior à data de término.")

        # Para edição, exclui a própria instância da verificação
        instance_id = self.instance.id if self.instance else None

        # Verifica conflitos de reserva
        conflito = ReservaAmbiente.objects.filter(
            sala_reservada=sala,
            periodo=periodo,
            data_inicio__lte=data_termino,
            data_termino__gte=data_inicio
        ).exclude(id=instance_id).exists()

        if conflito:
            raise serializers.ValidationError(
                f"Já existe uma reserva para a sala '{sala}' no período '{periodo}' entre {data_inicio} e {data_termino}."
            )

        return data

    
class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'tipo': self.user.tipo
        }
        return data