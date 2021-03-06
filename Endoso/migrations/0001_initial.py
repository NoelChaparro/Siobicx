# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeclaracionEndoso'
        db.create_table('declaracionendoso', (
            ('IdDeclaracionEndoso', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Constancia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Constancias.Constancia'])),
            ('FechaEndoso', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ExistenciaInicial', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('TarifaMensual', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('PeriodoInicio', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('PeriodoFin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('CierreMes', self.gf('django.db.models.fields.NullBooleanField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal(u'Endoso', ['DeclaracionEndoso'])

        # Adding model 'DeclaracionEndosoPorDia'
        db.create_table('declaracionendosopordia', (
            ('IdDeclaracionEndosoPorDia', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DeclaracionEndoso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Endoso.DeclaracionEndoso'])),
            ('Dia', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('Entrada', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('Salida', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('Precio', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('Existencia', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('Valor', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('TarifaMensual', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('TarifaDiaria', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('Cuota', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
        ))
        db.send_create_signal(u'Endoso', ['DeclaracionEndosoPorDia'])

        # Adding model 'Endoso'
        db.create_table('endoso', (
            ('IdEndoso', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DeclaracionEndoso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Endoso.DeclaracionEndoso'])),
            ('BienesAsegurados', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('SumaAsegurada', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('PorcentajeFondo', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('ImporteFondo', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('PorcentajeReaseguro', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('ImporteReaseguro', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('PorcentajeTotal', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
            ('ImporteTotal', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=4, blank=True)),
        ))
        db.send_create_signal(u'Endoso', ['Endoso'])


    def backwards(self, orm):
        # Deleting model 'DeclaracionEndoso'
        db.delete_table('declaracionendoso')

        # Deleting model 'DeclaracionEndosoPorDia'
        db.delete_table('declaracionendosopordia')

        # Deleting model 'Endoso'
        db.delete_table('endoso')


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
            'IdConstancia': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "('IdConstancia',)", 'object_name': 'Constancia', 'db_table': "'Constancia'"},
            'Solicitud': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Solicitud.Solicitud']"}),
            'SumaAsegurada': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '4', 'blank': 'True'}),
            'VigenciaFin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'VigenciaInicio': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'Endoso.declaracionendoso': {
            'CierreMes': ('django.db.models.fields.NullBooleanField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'Constancia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Constancias.Constancia']"}),
            'ExistenciaInicial': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'FechaEndoso': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'IdDeclaracionEndoso': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "('IdDeclaracionEndoso',)", 'object_name': 'DeclaracionEndoso', 'db_table': "'declaracionendoso'"},
            'PeriodoFin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'PeriodoInicio': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'TarifaMensual': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'})
        },
        u'Endoso.declaracionendosopordia': {
            'Cuota': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'DeclaracionEndoso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Endoso.DeclaracionEndoso']"}),
            'Dia': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'Entrada': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'Existencia': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'IdDeclaracionEndosoPorDia': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'Meta': {'ordering': "('IdDeclaracionEndosoPorDia',)", 'object_name': 'DeclaracionEndosoPorDia', 'db_table': "'declaracionendosopordia'"},
            'Precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'Salida': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'TarifaDiaria': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'TarifaMensual': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'Valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'})
        },
        u'Endoso.endoso': {
            'BienesAsegurados': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'DeclaracionEndoso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Endoso.DeclaracionEndoso']"}),
            'IdEndoso': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ImporteFondo': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'ImporteReaseguro': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'ImporteTotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'Meta': {'ordering': "('IdEndoso',)", 'object_name': 'Endoso', 'db_table': "'endoso'"},
            'PorcentajeFondo': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'PorcentajeReaseguro': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'PorcentajeTotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'}),
            'SumaAsegurada': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '4', 'blank': 'True'})
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
            'Meta': {'object_name': 'Programa', 'db_table': "'programas'"},
            'Observaciones': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'PersonaHabilitador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ConexosAgropecuarios.Persona']"}),
            'Utilizado': ('django.db.models.fields.NullBooleanField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['Endoso']