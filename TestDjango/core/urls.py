from django.urls import path
from .views import home, test, form

urlpatterns = [
    path ('', home,name="home"),
    path ('test/', test,name="tests"),
    path ('form_contacto/', form,name="form")
]