from django.db import models
import uuid


class Project(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    demo_link = models.CharField(max_length=2000,  null=True ,  blank=True)
    source_link =  models.CharField(max_length= 2000 ,  null=True ,  blank=True)
    tags = models.ManyToManyField('Tag' , blank=True)
    vote_total  = models.IntegerField(default=0 , null=True , blank=True)
    vote_ratio = models.IntegerField(default=0 , null=True ,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True)
    def __str__(self):
        return self.title



# one to many releationship used foreignkey

class Review(models.Model):

    VOTE_TYPE =(
        ('up', 'Up Vote'),
        ('down' , 'Down Vote'),
    )


    # ownner =
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True , blank=True)
    value = models.CharField(max_length=200 ,choices=VOTE_TYPE)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True)
    
    def __str__(self):
        return self.value



# many to many releationship


class Tag(models.Model):
    name =  models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True)
    def __str__(self):
        return self.name



       

