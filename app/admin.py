from django.contrib import admin
from .models import Article, Recipe
from .models import StripeCustomer


admin.site.register(StripeCustomer)


admin.site.register(Article)
admin.site.register(Recipe)
