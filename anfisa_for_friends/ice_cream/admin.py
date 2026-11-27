# ice_cream/admin.py
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category

from .models import Topping

from .models import Wrapper

from .models import IceCream


admin.site.register(Category)

admin.site.register(Topping)

admin.site.register(Wrapper)

admin.site.register(IceCream)
