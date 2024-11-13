from odoo import models, fields, api

class Curso(models.Model):
    _name = 'colegio.curso'
    _description = 'Curso del Colegio'
    _rec_name = '_grado_name'

    nombre = fields.Char("Nombre del Curso", required=True)
    nivel = fields.Char("Nivel del Curso", required=True)
    alumno_ids = fields.One2many('colegio.alumno', 'grado', string="Alumnos")
    asignacion_ids = fields.One2many('colegio.asignacion', 'curso_id', string="Asignaciones")
    
    # Campo computado para concatenar nombre y nivel
    _grado_name = fields.Char(compute='_compute_name', store=False)

    @api.depends('nombre', 'nivel')
    def _compute_name(self):
        for record in self:
            record._grado_name = f"{record.nombre} - {record.nivel}"
