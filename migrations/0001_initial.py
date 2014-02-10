# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VoteCount'
        db.create_table(u'quirktonomicon_votecount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accessed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('idea_id', self.gf('django.db.models.fields.IntegerField')()),
            ('votes_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_votes_needed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('considered_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'quirktonomicon', ['VoteCount'])

        # Adding model 'Ideation'
        db.create_table(u'quirktonomicon_ideation', (
            ('app_enabled', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('considered_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('current_user_hidden', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('expires_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('features', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('idea_id', self.gf('django.db.models.fields.IntegerField')()),
            ('media', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('not_chosen_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('patent_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('problem', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('similar_products', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('solution', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('total_votes_needed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('under_consideration', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('votes_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'quirktonomicon', ['Ideation'])


    def backwards(self, orm):
        # Deleting model 'VoteCount'
        db.delete_table(u'quirktonomicon_votecount')

        # Deleting model 'Ideation'
        db.delete_table(u'quirktonomicon_ideation')


    models = {
        u'quirktonomicon.ideation': {
            'Meta': {'ordering': "['expires_at']", 'object_name': 'Ideation'},
            'app_enabled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'considered_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'current_user_hidden': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idea_id': ('django.db.models.fields.IntegerField', [], {}),
            'media': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'not_chosen_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'patent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'problem': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'similar_products': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'solution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'total_votes_needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'under_consideration': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'quirktonomicon.votecount': {
            'Meta': {'ordering': "['accessed_at']", 'object_name': 'VoteCount'},
            'accessed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'considered_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea_id': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'total_votes_needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quirktonomicon']