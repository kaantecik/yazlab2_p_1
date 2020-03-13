from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from users.views import *
from django.contrib.auth import views as auth_views

# URL'lerin tanımlandığı alan. Parametre olarak kullanacağı fonksiyonu alır.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accounts/profile/uploadbook/', upload_book, name="upload_book"),
    path('accounts/profile/', profile, name="profile"),
    path('books/', books, name="books"),
    path('accounts/delete/<int:id>/', deleteuser, name="delete_user"),
    path('books/delete/<int:id>/', deletebook, name="delete_book"),
    path('books/return/<int:id>/', returnbook, name="return_book"),
    path('books/lend/<int:id>/', lendbook, name="lend_book"),
    path('books/update/<int:id>/', update_book, name="update_book"),
    path('settings/', settingspage, name="settings"),
    path('register/', register, name="register"),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name="forms/login.html"), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(
        template_name="forms/logout.html"), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
