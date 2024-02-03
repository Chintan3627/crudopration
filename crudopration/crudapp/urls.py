from django.urls import path
from . import views
urlpatterns =[

        path('get', views.PostCrudView.as_view(),name = "get"),
        path('post', views.PostCrudView.as_view(),name = "post"),
        path('delete/<int:pk>', views.PostCrudView.as_view(),name = "delete"),
        path('edit/<int:pk>', views.PostCrudView.as_view(),name = "edit"),
]