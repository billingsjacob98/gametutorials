# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('tutorials_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('game_engine', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('review', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('tutorials', ['Game'])

        # Adding model 'Mission'
        db.create_table('tutorials_mission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tutorials.Game'])),
        ))
        db.send_create_signal('tutorials', ['Mission'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('tutorials_game')

        # Deleting model 'Mission'
        db.delete_table('tutorials_mission')


    models = {
        'tutorials.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.TextField', [], {}),
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