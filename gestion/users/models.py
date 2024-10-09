from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        permissions = [   # la palabra permissions es una palabra reservada y tiene q ser escrita asi 
            ('view_ventas','Puede ver la seccion de Venta'),
            ('view_compras','Puede ver la seccion de compra'),
            ('view_inventarios', 'Puede ver la seccion de Inventarios'),
            ('view_reportes','Puede ver la seccion de Reportes'),
            ('view_finanzas','Puede ver la seccion de Finanzas'),
        ]

# Create your models here.
