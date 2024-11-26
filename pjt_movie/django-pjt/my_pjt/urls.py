"""
URL configuration for my_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/movies/', include('movies.urls')),

    # custom 이후 링크
    path('accounts/', include('accounts.urls'))

    # 기존 accounts 링크
    # path('accounts/', include('dj_rest_auth.urls')), # 회원가입과 관련한 인증
    # path('accounts/signup/', include('dj_rest_auth.registration.urls')), # 나머지
]

# 프로필 사진 띄우기 위함
if settings.DEBUG:  # 개발 환경에서만 미디어 파일 서빙
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
