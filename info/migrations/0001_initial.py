# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InfoPage'
        db.create_table('info_infopage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['info.InfoPage'])),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content_en', self.gf('tinymce.models.HTMLField')()),
            ('title_ru', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content_ru', self.gf('tinymce.models.HTMLField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='page', max_length=15)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('info', ['InfoPage'])


    def backwards(self, orm):
        # Deleting model 'InfoPage'
        db.delete_table('info_infopage')


    models = {
        'info.infopage': {
            'Meta': {'object_name': 'InfoPage'},
            'content_en': ('tinymce.models.HTMLField', [], {}),
            'content_ru': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['info.InfoPage']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'page'", 'max_length': '15'})
        }
    }

    complete_apps = ['info']