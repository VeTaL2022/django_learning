from django.urls import path

from .views import AddPhotoToCar, CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>/photo', AddPhotoToCar.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view())
]
