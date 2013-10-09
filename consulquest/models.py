from django.db import models

# Create your models here.

class Association(models.Model):
    """An association involved in the consultation nationale"""

    name = models.CharField(max_length=200,
                            verbose_name="Nom de l'association")
    mail = models.CharField(max_length=200)    

    inscr_date = models.DateTimeField('Inscritption')
    inscr_confirmed = models.BooleanField(default=0) 

    password = models.CharField(max_length=200)    
    def __unicode__(self):  
        return self.name

class Question(models.Model):
    """ A question submited to the vote"""
    author = models.ForeignKey(Association)
    text = models.CharField(max_length=200)
    date = models.DateTimeField('Date de la proposition')
    def __unicode__(self):  
        return self.text

class Vote(models.Model):
    """ A vote by an association for a question"""
    author = models.ForeignKey(Association)
    question = models.ForeignKey(Question)
    date = models.DateTimeField('Date du vote')
    value = models.IntegerField(default=0) 
    def __unicode__(self):  
        return "Vote de " + self.author.name + " pour " + self.question.text
