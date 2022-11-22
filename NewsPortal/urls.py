from django.urls import path
from .views import PostsList, PostList, PostsSearch


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostList.as_view()),
   path('search/', PostsSearch.as_view())
]
