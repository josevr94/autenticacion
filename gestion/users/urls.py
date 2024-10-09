from django.urls import path
from users import views
from django.conf.urls import handler403
    


urlpatterns = [
    path('register/',views.login,name='register'),
    path('account/login/',views.login_view,name='login'),
    path('ventas/',views.ventas_view,name='ventas'),
    path('compras/',views.compras_view,name='compras'),
    path('inventario/',views.inventario_view,name='inventario'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.home,name='home'),
    path('reportes/',views.reportes_view,name='reportes'),
    path('finanzas/',views.finanzas_view,name='finanzas'),
]

handler403 ='users.views.custom_403_view'

