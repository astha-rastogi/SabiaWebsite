from django.conf.urls import url
from homepage import views
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^tutorForm/$', views.SubmitTutorFormPageView.as_view()),
    url(r'^tutorForm/send/$', views.submitTutorForm),
    url(r'^allTutors/$',views.AllTutorsView.as_view()),
    url(r'^createAccount/$',views.CreateAccountView.as_view()),
    url(r'^createAccount/submit/$',views.createAccount),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^login/submit/$', views.login),
    url(r'^dashboard/$', views.DashboardView.as_view())

]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)