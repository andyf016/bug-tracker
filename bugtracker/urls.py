"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from bugapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('newticket/', views.ticket_form_view, name='ticketform'),
    path('author/<int:author_id>/', views.author_detail, name='authordetail'),
    path('ticketdetail/<int:ticket_id>/edit', views.ticket_edit_view, name='edit'),
    path('ticketdetail/<int:ticket_id>/', views.ticket_detail_view, name='details'),
    path('assign/<int:ticket_id>/', views.assign_view, name='assign'),
    path('invalid/<int:ticket_id>/', views.invalid_view, name='invalid'),
    path('done/<int:ticket_id>/', views.done_view, name='done'),
    path('return/<int:ticket_id>/', views.return_view, name='return'),
    path('admin/', admin.site.urls),
]
