from django.urls import path, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static
# from django_apscheduler import urls as apscheduler_urls
app_name = "user"

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view,name="logout"),
    path("signup", views.signup_view, name="signup"),
    path('decision/', views.salad_decision, name='decision'),
    path('diet/',views.profile,name="diet"),
    path('editdiet/', views.upload,name="editdiet"),
    path('editdiet_create/', views.upload_create,name="editdiet_create"),
    # path('apscheduler/', include(apscheduler_urls)),
    
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)