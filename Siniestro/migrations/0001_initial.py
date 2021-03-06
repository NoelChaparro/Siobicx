# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AvisoSiniestro'
        db.create_table('avisosiniestro', (
            ('IdAvisoSiniestro', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Constancia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Constancias.Constancia'])),
            ('FechaAviso', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('FechaSiniestro', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('PersonaAvisa', self.gf('django.db.models.fields.related.ForeignKey')(related_name='PersonaAviso', to=orm['ConexosAgropecuarios.Persona'])),
            ('PersonaTecnico', self.gf('django.db.models.fields.related.ForeignKey')(related_name='PersonaTecnico', to=orm['ConexosAgropecuarios.Persona'])),
            ('NombreAvisa', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('NumeroAviso', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ViaAviso', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('DescripcionBienAfectado', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('HoraAviso', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('HoraSiniestro', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('OtraVia', self.gf('django.db.models.fields.NullBooleanField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal(u'Siniestro', ['AvisoSiniestro'])

        # Adding model 'ImagenSiniestro'
        db.create_table('ImagenSiniestro', (
            ('IdImagenSiniestro', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('DateAdded', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'Siniestro', ['ImagenSiniestro'])


    def backwards(self, orm):
        # Deleting model 'AvisoSiniestro'
        db.delete_table('avisosiniestro')

        # Deleting model 'ImagenSiniestro'
        db.delete_table('ImagenSiniestro')


    models = {
        u'ConexosAgropecuarios.persona': {
            'ApellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ApellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Curp': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'EsSocio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'EstadoCivil': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'FechaIngreso': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FechaNacimiento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'IdPersona': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "('Rfc',)", 'object_name': 'Persona', 'db_table': "'Personas'"},
            'PrimerNombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'RazonSocial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Rfc': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'SegundoNombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'TipoPersona': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'})
        },
        u'Constancias.constancia': {
            'CuotaNeta': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'Estatus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'FechaEmision': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FechaPago': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FolioConstancia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'FormaPago': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'IdConstancia': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "('IdConstancia',)", 'object_name': 'Constancia', 'db_table': "'Constancia'"},
            'Solicitud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Solicitud.Solicitud']"}),
            'SumaAsegurada': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'Utilizado': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'UtilizadoDeclaracion': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'VigenciaFin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'VigenciaInicio': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Programas.programa': {
            'Ejercicio': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'FechaPrograma': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FolioPrograma': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'IdContratoFondo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'IdPrograma': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'IdSubTipoSeguro': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'IdTipoMoneda': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'IdTipoSeguro': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Programa', 'db_table': "'Programas'"},
            'Observaciones': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'PersonaHabilitador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'Utilizado': ('django.db.models.fields.NullBooleanField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        u'Siniestro.avisosiniestro': {
            'Constancia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Constancias.Constancia']"}),
            'DescripcionBienAfectado': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'FechaAviso': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FechaSiniestro': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'HoraAviso': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'HoraSiniestro': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'IdAvisoSiniestro': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'object_name': 'AvisoSiniestro', 'db_table': "'avisosiniestro'"},
            'NombreAvisa': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'NumeroAviso': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'OtraVia': ('django.db.models.fields.NullBooleanField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'PersonaAvisa': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PersonaAviso'", 'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'PersonaTecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PersonaTecnico'", 'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'ViaAviso': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'Siniestro.imagensiniestro': {
            'DateAdded': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'IdImagenSiniestro': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'Meta': {'ordering': "('IdImagenSiniestro',)", 'object_name': 'ImagenSiniestro', 'db_table': "'ImagenSiniestro'"}
        },
        u'Solicitud.solicitud': {
            'DeclaracionSolicitud': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'Estatus': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'FechaSolicitud': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'FolioSolicitud': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'IdSolicitud': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "('IdSolicitud',)", 'object_name': 'Solicitud', 'db_table': "'Solicitud'"},
            'Observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'PersonaAsegurada': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PersonaAsegurada'", 'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'PersonaContratante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PersonaContratante'", 'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'PersonaSolicitante': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'PersonaSolicitante'", 'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'Programa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Programas.Programa']"}),
            'Unidades': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ValorUnidad': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['Siniestro']