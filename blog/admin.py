from django.contrib import admin
from .models import Post

admin.site.register(Post)

admin.site.site_header = 'Tha blog'
admin.site.site_title = 'Tha Blog'
admin.site.index_title = 'Tha blog'
