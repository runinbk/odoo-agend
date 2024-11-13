from odoo import models, fields

class Gestion(models.Model):
    _name = 'colegio.gestion'
    _description = 'Gestión de Inscripciones y Asignaciones'
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre de la Gestión", required=True)
    fecha_inicio = fields.Date('Fecha de Inicio', required=True)
    fecha_fin = fields.Date('Fecha Finalización')
    asignacion_ids = fields.One2many('colegio.asignacion', 'gestion_id', string="Asignaciones")
