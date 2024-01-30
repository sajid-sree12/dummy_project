from django.urls import path
from . import views
urlpatterns=[
    path("call1/support1",views.home,name="home"),
    path("call2",views.home2,name="home2"),
    path("call3",views.home3,name="home3"),
    path("wish/<str:name>",views.greet,name="greet_name"),
    path("<int:old>",views.greet2,name="greet2"),
    path("movie",views.form_view,name="form_name"),
]