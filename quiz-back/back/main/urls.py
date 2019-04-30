from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/posts/', views.PostView.as_view()),
    path('main/posts/<int:pk>/', views.PostDetailView.as_view()),
    path('main/posts/<int:pk>/like/', views.PostLike.as_view()),
    path('login/', views.login),
    path('logout/', views.logout)
]