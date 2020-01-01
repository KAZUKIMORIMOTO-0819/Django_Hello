from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloWorldView

### 指示書
urlpatterns = [
    path('admin/', admin.site.urls),  # admin/ を受けると、adomin.site.urlsを返す
    path("hello/", include("helloworldapp.urls"))   # アプリ内のurls.pyにつなげる
]
