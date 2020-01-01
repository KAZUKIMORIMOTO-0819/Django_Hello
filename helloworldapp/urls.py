from django.urls import path
from .views import hellofunction

### 指示書
urlpatterns = [
    path("world/", hellofunction),   # 追加 helloworldfunctionを起動する
]