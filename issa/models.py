from django.db import models
from pyuploadcare.dj.models import ImageField
from django.http import Http404
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist




# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    occupants_count = models.IntegerField()
    picture = models.ImageField(upload_to = 'activis/', null=True)

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()   

    @classmethod
    def update_neighbourhood(cls,neighbourhood,update):
         updated = cls.objects.filter(neighbourhood_name=neighbourhood).update(name=update)
         return updated

    @classmethod
    def update_occupants_count(cls,occupants_count,update):
         updated = cls.objects.filter(occupants_count=occupants_count).update(name=update)
         return updated


    def __str__(self):
        return self.neighbourhood_name




class Profile(models.Model):
    name = models.CharField(max_length = 60)
    user_Id =models.IntegerField(default = 0)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    user_email = models.EmailField()


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()   


    @classmethod
    def find_profile(cls, user_id):
        Profile = cls.objects.get(id=user_id)
        return profile

    @classmethod
    def update_profile(cls,user,update):
         updated = cls.objects.filter(name=user).update(name=update)
         return updated

    def __str__(self):
        return self.full_name

class Business(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    neighbourhood_business = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    business_email = models.EmailField()
    business_picture = models.ImageField(upload_to = 'stoptrynabegod/')

    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        Businesses.objects.filter().delete()

    @classmethod
    def get_business(cls, post_id):
        single_business = cls.objects.get(id=post_id)
        return single_business

    @classmethod
    def get_businesses(cls):
        businesses = Businesses.objects.all()
        return businesses


    class Meta:
        ordering = ['-id']


class Activity(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='profile')
    title = models.CharField(max_length = 60)
    activity = models.TextField(blank= True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    submitter_id = models.IntegerField(default=0)

    def save_activity(self):
        self.save()

    def delete_activity(self):
        Activities.objects.filter().delete()
    
    @classmethod
    def get_activities(cls):
        Activities = Activity.objects.all()
        return activities

    @classmethod
    def get_activity(cls, post_id):
        single_activity = cls.objects.get(id=post_id)
        return single_activity

    @classmethod
    def search_by_title(cls,search_term):
        activity = cls.objects.filter(title__icontains=search_term)
        return activity

    class Meta:
        ordering = ['-id']

    
    def __str__(self):
        return self.title
