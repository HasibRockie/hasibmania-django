from django.db import models
import datetime

CATEGORIES = (
    ('ব্যক্তিগত','ব্যক্তিগত'),
    ('ব্লগ', 'ব্লগ'),
    ('ধর্মীয়','ধর্মীয়'),
    ('ফিকশন','ফিকশন'),
    ('অন্যান্য','অন্যান্য'),
)

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='ব্যক্তিগত')
    title = models.CharField(max_length=400)
    para1 = models.TextField(blank=True)
    para2 = models.TextField(blank=True)
    para3 = models.TextField(blank=True)
    para4 = models.TextField(blank=True)
    para5 = models.TextField(blank=True)
    para6 = models.TextField(blank=True)
    para7 = models.TextField(blank=True)
    para8 = models.TextField(blank=True)
    para9 = models.TextField(blank=True)
    para10 = models.TextField(blank=True)
    para11 = models.TextField(blank=True)
    para12 = models.TextField(blank=True)
    para13 = models.TextField(blank=True)
    para14 = models.TextField(blank=True)
    para15 = models.TextField(blank=True)
    para16 = models.TextField(blank=True)
    para17 = models.TextField(blank=True)
    para18 = models.TextField(blank=True)
    para19 = models.TextField(blank=True)
    para20 = models.TextField(blank=True)
    para21 = models.TextField(blank=True)
    para22 = models.TextField(blank=True)
    para23 = models.TextField(blank=True)
    para24 = models.TextField(blank=True)
    para25 = models.TextField(blank=True)
    img1 = models.ImageField(upload_to ='static/uploads', blank=True)
    img1caption = models.CharField(max_length=500, blank=True)
    img2 = models.ImageField(upload_to ='static/uploads', blank=True)
    img2caption = models.CharField(max_length=500, blank=True)
    img3 = models.ImageField(upload_to ='static/uploads', blank=True)
    img3caption = models.CharField(max_length=500, blank=True)
    img4 = models.ImageField(upload_to ='static/uploads', blank=True)
    img4caption = models.CharField(max_length=500, blank=True)
    img5 = models.ImageField(upload_to ='static/uploads', blank=True)
    img5caption = models.CharField(max_length=500, blank=True)
    img6 = models.ImageField(upload_to ='static/uploads', blank=True)
    img6caption = models.CharField(max_length=500, blank=True)
    img7 = models.ImageField(upload_to ='static/uploads', blank=True)
    img7caption = models.CharField(max_length=500, blank=True)
    img8 = models.ImageField(upload_to ='static/uploads', blank=True)
    img8caption = models.CharField(max_length=500, blank=True)
    img9 = models.ImageField(upload_to ='static/uploads', blank=True)
    img9caption = models.CharField(max_length=500, blank=True)
    img10 = models.ImageField(upload_to ='static/uploads', blank=True)
    img10caption = models.CharField(max_length=500, blank=True)
    author = models.CharField(max_length=264, default='Hasibul Islam')

    def __str__(self):
        return self.title  

class Gratitude(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=264)
    gender = models.CharField(max_length=100, choices=(('male','male'),('female','female')), default='male')
    relation = models.CharField(max_length=264)
    img = models.ImageField(upload_to ='static/uploads/dedicated', blank=True, default='static/uploads/dedicated/male.png')
    dedicated = models.TextField()
    
    def __str__(self):
        return self.name 
