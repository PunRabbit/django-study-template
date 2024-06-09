from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from typing import List

from tutorial.snippets import views
from tutorial.snippets import class_view


urlpatterns: List[path] = [
    path('snippets', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('class-snippets', class_view.SnippetList.as_view()),
    path('class-snippets/<int:pk>/', class_view.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
