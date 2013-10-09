from django.contrib import admin
import consulquest.models as cq 

admin.site.register(cq.Association)
admin.site.register(cq.Question)
admin.site.register(cq.Vote)
