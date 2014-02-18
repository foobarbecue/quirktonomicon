# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Ideation', fields ['idea_id']
        db.create_index(u'quirktonomicon_ideation', ['idea_id'])

        # Adding index on 'Ideation', fields ['title']
        db.create_index(u'quirktonomicon_ideation', ['title'])

        # Adding index on 'VoteCount', fields ['accessed_at']
        db.create_index(u'quirktonomicon_votecount', ['accessed_at'])

        # Adding index on 'VoteCount', fields ['state']
        db.create_index(u'quirktonomicon_votecount', ['state'])

        # Adding index on 'HourData', fields ['start_time']
        db.create_index(u'quirktonomicon_hourdata', ['start_time'])


    def backwards(self, orm):
        # Removing index on 'HourData', fields ['start_time']
        db.delete_index(u'quirktonomicon_hourdata', ['start_time'])

        # Removing index on 'VoteCount', fields ['state']
        db.delete_index(u'quirktonomicon_votecount', ['state'])

        # Removing index on 'VoteCount', fields ['accessed_at']
        db.delete_index(u'quirktonomicon_votecount', ['accessed_at'])

        # Removing index on 'Ideation', fields ['title']
        db.delete_index(u'quirktonomicon_ideation', ['title'])

        # Removing index on 'Ideation', fields ['idea_id']
        db.delete_index(u'quirktonomicon_ideation', ['idea_id'])


    models = {
        u'quirktonomicon.flag': {
            'Meta': {'object_name': 'Flag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirktonomicon.Ideation']"}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'quirktonomicon.hourdata': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'HourData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_ideas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'new_votes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        },
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
            'funny': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'idea_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'junk': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'media': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'not_chosen_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'patent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'problem': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'similar_products': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'solution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_index': 'True'}),
            'total_votes_needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'under_consideration': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_in_latest_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'quirktonomicon.votecount': {
            'Meta': {'ordering': "['accessed_at']", 'object_name': 'VoteCount'},
            'accessed_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'considered_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea_id': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'total_votes_needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quirktonomicon']