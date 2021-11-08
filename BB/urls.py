from django.urls import path
from .views import BBList, BBDetail

urlpatterns = [
    path('list/', BBList.as_view()),
    path('detail/<int:pk>', BBDetail.as_view()),
]