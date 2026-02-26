"""
URL configuration for projeto_crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from crm.views import (
    ProdutoList, ProdutoCreate, ProdutoUpdate, ProdutoDelete, dashboard_crm
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_crm, name='dashboard'),
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
    path('produtos/novo/', ProdutoCreate.as_view(), name='produto-create'),
    path('produtos/editar/<int:pk>/', ProdutoUpdate.as_view(), name='produto-update'),
    path('produtos/remover/<int:pk>/', ProdutoDelete.as_view(), name='produto-delete'),
]
