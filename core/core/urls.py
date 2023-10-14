from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns.append(re_path("^finance/",include("finance.urls")))
urlpatterns.append(re_path("^logs/",include("logs.urls")))

