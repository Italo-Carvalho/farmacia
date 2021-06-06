from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('loja/', loja, name='loja'),
    path('funcionario/delete/<int:pk>', deletar_funcionario, name='deletar_funcionario'),
    path('produto/delete/<int:pk>', deletar_produto, name='deletar_produto'),
    path('produto/fila/delete/', deletar_ordem_em_fila, name='deletar_ordem_em_fila'),
    path('ordem/<int:produto_pk>/<int:user_pk>', compra_produto, name='compra_produto'),
    path('compras-chart/', compras_chart, name='compras-chart'),
    path('compras_quicksort_chart/', compras_quicksort_chart, name='compras_quicksort_chart'),
]
