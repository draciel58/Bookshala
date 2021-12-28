"""bookshala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from book import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('auth/',views.authpage,name="authpage"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginuser,name="loginuser"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('main/',views.main,name="main"),
    path('book/<int:book_pk>/',views.viewbook,name="viewbook"),
    path('addbook/',views.addbook,name="addbook"),
    path('wishlist/',views.wishlist,name="wishlist"),
    path('yourbooks/',views.yourbooks,name="yourbooks"), 
    path('deletebook/<int:book_pk>/',views.deletebook,name="deletebook"), 
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
