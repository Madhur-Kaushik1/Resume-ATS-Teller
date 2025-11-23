from django.db import models
    
class resume_model(models.Model):
    file = models.FileField(upload_to='resume')
    name = models.CharField(max_length=100, blank=True)

    def save(self,*args, **kwargs):
        if not self.name:
            count = resume_model.objects.count()
            self.name = f'resume{count + 1}'
        super().save(*args, **kwargs)