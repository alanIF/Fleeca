from django.db import models
from django.utils import timezone

# Create your models here.

class Log(models.Model):
    description = models.TextField()
    app = models.TextField()
    model = models.TextField()
    object_id = models.TextField()
    user = models.TextField()
    created = models.DateTimeField(default=timezone.now, editable=False)

    def add(description :str, app:str, model:str , object_id:str, user:str)->None:
        log:Log = Log (description =description ,app=app,model=model,object_id=object_id,user=user)
        log.save()
