from django.db import models

class Project(models.Model):
    TECH = (('flutter','Flutter'),
            ('react','React'),
            ('django','Django'),
            ('flask','Flask'))

    title = models.CharField(max_length = 100)
    description = models.TextField()
    technology = models.CharField(choices = TECH,max_length = 20,default = None )
    image = models.FileField(upload_to = 'image')
