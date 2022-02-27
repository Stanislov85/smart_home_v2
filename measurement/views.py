# TODO: опишите необходимые обработчики, рекомендуется
#  использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementCreateSerializer, SensorDetailSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class SensorView_get_post(ListCreateAPIView):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorView_get_patch(RetrieveUpdateDestroyAPIView):
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(CreateAPIView):
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer

