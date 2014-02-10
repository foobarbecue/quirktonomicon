# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flag'
        db.create_table(u'quirktonomicon_flag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('idea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirktonomicon.Ideation'])),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'quirktonomicon', ['Flag'])

        # Adding field 'Ideation.funny'
        db.add_column(u'quirktonomicon_ideation', 'funny',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Ideation.junk'
        db.add_column(u'quirktonomicon_ideation', 'junk',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Flag'
        db.delete_table(u'quirktonomicon_flag')

        # Deleting field 'Ideation.funny'
        db.delete_column(u'quirktonomicon_ideation', 'funny')

        # Deleting field 'Ideation.junk'
        db.delete_column(u'quirktonomicon_ideation', 'junk')


    models = {
        u'quirktonomicon.flag': {
            'Meta': {'object_name': 'Flag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirktonomicon.Ideation']"}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '5'})
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
            'idea_id': ('django.db.models.fields.IntegerField', [], {}),
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'total_votes_needed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'under_consideration': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'votes_in_latest_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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