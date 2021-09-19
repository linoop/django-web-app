from django.urls import path
from blog.views import (
    createBlogView,
    detailBlogView,
    edit_blog_view
)

app_name = 'blog'

urlpatterns = [
    path('create/', createBlogView, name="create"),
    path('<slug>/', detailBlogView, name="detail"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
]
