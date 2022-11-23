from django.contrib import admin

from beers.models import Beer, Review, Comment

admin.site.register(Beer)
admin.site.register(Review)
admin.site.register(Comment)

