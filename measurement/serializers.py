from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from .models import Sensor,Measurement

class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'value', 'created_data']


class MeasurementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['value', 'created_data']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementListSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
