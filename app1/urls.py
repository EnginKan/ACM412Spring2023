from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("allbooks",views.getAllBooks),
    path(r'bookdetails/<int:id>',views.getBookByID, name="bookbyid")
]