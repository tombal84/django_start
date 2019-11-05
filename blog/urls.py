from django.urls import path
from django_first_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index)
]