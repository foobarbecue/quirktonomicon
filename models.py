from django.db import models

# Create your models here.
class VoteCount(models.Model):
    accessed_at = models.DateTimeField(blank=True, null=True, db_index=True)
    idea = models.ForeignKey('Ideation', to_field='idea_id')
    votes_count = models.IntegerField(blank=True, null=True)
    total_votes_needed = models.IntegerField(blank=True, null=True)
    considered_at = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=30, db_index=True)
    
    def __str__(self):
        return unicode(self.votes_count)
    
    class Meta:
        ordering = ['accessed_at']
        get_latest_by = 'accessed_at'

class Ideation(models.Model):
    app_enabled = models.NullBooleanField(blank=True, null=True)
    category = models.CharField(max_length=30)
    considered_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    current_user_hidden = models.NullBooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    idea_id = models.IntegerField(db_index=True, unique=True)
    media = models.TextField(blank=True, null=True)
    not_chosen_at = models.DateTimeField(blank=True, null=True)
    patent_id = models.IntegerField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    similar_products = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=30)
    title = models.CharField(max_length=500, db_index=True)
    total_votes_needed = models.IntegerField(blank=True, null=True)
    under_consideration = models.NullBooleanField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    votes_count = models.IntegerField(blank=True, null=True) #not canonical
    votes_in_latest_day=models.IntegerField(blank=True, null=True) #not canonical
    funny=models.IntegerField(default=0) #not canonical
    junk=models.IntegerField(default=0) #not canonical
    
    def get_latest_vote_count(self):
        VoteCount.objects.filter(idea_id=self.idea_id).latest()

    def get_absolute_url(self):
        return '/ideas/%s' % self.idea_id

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['expires_at']

class Flag(models.Model):
    ip_address=models.IPAddressField()
    idea=models.ForeignKey('Ideation')
    KIND_CHOICES=(('junk','junk'),('funny','funny'))
    kind=models.CharField(max_length=5,choices=KIND_CHOICES)

class HourData(models.Model):
    start_time=models.DateTimeField(db_index=True)
    new_votes=models.IntegerField(blank=True, null=True)
    new_ideas=models.IntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ["start_time"]
        get_latest_by = "start_time"
    
#class VoteDiff(models.Model):
    #calculated_at=
    #start_time=
    #end_time=