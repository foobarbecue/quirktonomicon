from django.db import models

# Create your models here.
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

    def __str__(self):
        self.title

class VoteCount(models.Model):
    accessed_at = models.DateTimeField(blank=True, null=True)
    idea_id = models.IntegerField()
    votes_count = models.IntegerField(blank=True, null=True)
    total_votes_needed = models.IntegerField(blank=True, null=True)
    considered_at = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=30)