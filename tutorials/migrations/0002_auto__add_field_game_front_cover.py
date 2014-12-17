# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.front_cover'
        db.add_column('tutorials_game', 'front_cover',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.front_cover'
        db.delete_column('tutorials_game', 'front_cover')


    models = {
        'tutorials.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'front_cover': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'game_engine': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'review': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'tutorials.mission': {
            'Meta': {'object_name': 'Mission'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tutorials.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tutorials']