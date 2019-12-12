from django.urls import path
from .views import *

urlpatterns = [
    #         generic 은 화면을 호출할 떄 as_view()를 넣어줘야 한다.
    path('', BookmarkLsit.as_view(), name="list"),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name="delete")
]