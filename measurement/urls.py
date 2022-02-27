from django.urls import path

from .views import SensorView_get_post, MeasurementCreateView, SensorView_get_patch

urlpatterns = [
    path('api/sensors/', SensorView_get_post.as_view()),
    path('api/sensors/<int:pk>/', SensorView_get_patch.as_view()),
    path('api/measurement/', MeasurementCreateView.as_view()),
    ]
