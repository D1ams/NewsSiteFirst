from django.urls import path
from .views import PostsList, PostList


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostList.as_view())
]
