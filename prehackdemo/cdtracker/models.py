from django.db.models import *

class Artist(Model):
    name          = CharField(max_length=60)
    date_of_birth = DateField()
    
    def __unicode__(self):
        """This function gives it a meaningful output when we print an Artist object"""
        return self.name
    

class Album(Model):
    name       = CharField(max_length=24)
    artist     = ForeignKey(Artist)
    num_tracks = IntegerField()
    
    def __unicode__(self):
        """This function gives a meaningful output when we print an Album object"""
        return self.name
    