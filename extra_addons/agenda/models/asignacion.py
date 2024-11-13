from odoo import models, fields

class Asignacion(models.Model):
    _name = 'colegio.asignacion'
    _description = 'Asignación de Cursos, Materias y Profesores'

    curso_id = fields.Many2one('colegio.curso', string="Curso", required=True)
    materia_id = fields.Many2one('colegio.materia', string="Materia", required=True)
    profesor_id = fields.Many2one('colegio.profesor', string="Profesor", required=True)
    gestion_id = fields.Many2one('colegio.gestion', string="Gestión")
