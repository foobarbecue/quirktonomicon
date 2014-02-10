from django.db import models

# Create your models here.
class VoteCount(models.Model):
    accessed_at = models.DateTimeField(blank=True, null=True)
    idea_id = models.IntegerField()
    votes_count = models.IntegerField(blank=True, null=True)
    total_votes_needed = models.IntegerField(blank=True, null=True)
    considered_at = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=30)
    
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
    idea_id = models.IntegerField()
    media = models.TextField(blank=True, null=True)
    not_chosen_at = models.DateTimeField(blank=True, null=True)
    patent_id = models.IntegerField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    similar_products = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=30)
    title = models.CharField(max_length=500)
    total_votes_needed = models.IntegerField(blank=True, null=True)
    under_consideration = models.NullBooleanField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    votes_count = models.IntegerField(blank=True, null=True)
    votes_in_latest_day=models.IntegerField(blank=True, null=True)    
    
    def get_latest_vote_count(self):
        VoteCount.objects.filter(idea_id=self.idea_id).latest()

    def get_absolute_url(self):
        return '/ideas/%s' % self.idea_id

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['expires_at']

#class VoteDiff(models.Model):
    #calculated_at=
    #start_time=
    #end_time=