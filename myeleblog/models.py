from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(blank=True, null=True, upload_to='images/')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=250)
    likes = models.ManyToManyField(User,related_name='blog_post')
   
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return  reverse('detail_view',args=[str(self.id)])   



class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=200,null=True,blank=True,default=None)
    whatsapp_url = models.CharField(max_length=200,null=True,blank=True,default=None)
    facebook_url = models.CharField(max_length=200,null=True,blank=True,default=None)
    insta_url = models.CharField(max_length=200,null=True,blank=True,default=None)
    twitter_url = models.CharField(max_length=200,null=True,blank=True,default=None)
    
    def __str__(self):
       return str(self.user) 
    
    def get_absolute_url(self):
       return  reverse('home')   