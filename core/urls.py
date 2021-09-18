from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('article',views.ArticleView.as_view(),name='article'),
    path('privacy',views.PrivacyView.as_view(),name='privacy'),
    path('terms',views.TermsView.as_view(),name='terms'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('login',views.LoginView.as_view(),name='login'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)