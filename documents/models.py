from django.db import models
from django.template.defaultfilters import slugify
import uuid
from django.core.validators import FileExtensionValidator



# Create your models here.

class Folders(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    trash = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Folders, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class SubFolders(models.Model):
    name = models.CharField(max_length=25)
    folders = models.ForeignKey(Folders, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='files/', validators=[FileExtensionValidator(['pdf','docx','doc'])], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    trash = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubFolders, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    
class Documents(models.Model):
    title = models.CharField(max_length=30)
    uploaded_by = models.CharField(max_length=35)
    upload_date = models.DateTimeField(auto_now_add=True)
    upload_file = models.FileField(upload_to='file/', validators=[FileExtensionValidator(['pdf','docx','doc'])],null=True, blank=True)
    image = models.ImageField(upload_to= 'image/', blank=True, null=True)
    description = models.TextField()
    trash = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,default=uuid.uuid1)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Documents, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
