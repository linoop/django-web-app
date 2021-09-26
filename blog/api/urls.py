from django.urls import path
from blog.api.views import (
    apiDetailBlogView,
    apiUpdateBlogView,
    apiCreateBlogView,
    apiDeleteBlogView,
)

app_name = 'blog'

urlpatterns = [
    path('<slug>/', apiDetailBlogView, name='detail'),
    path('<slug>/update', apiUpdateBlogView, name='update'),
    path('<slug>/delete', apiDeleteBlogView, name='delete'),
    path('create', apiCreateBlogView, name='create'),
]
