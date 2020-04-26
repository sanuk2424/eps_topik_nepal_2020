from django.contrib import admin

# Register your models here.
from practice_question.models import ImageTypeQuestion, FillingTypeQuestion, PassageTypeQuestion

admin.site.register(ImageTypeQuestion)
admin.site.register(FillingTypeQuestion)
admin.site.register(PassageTypeQuestion)
