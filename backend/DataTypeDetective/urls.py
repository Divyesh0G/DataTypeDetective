
from django.urls import path
from .views import InferDataTypesView

urlpatterns = [
    path('', InferDataTypesView.as_view(), name='infer_data_types'),
]
