from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'colegio.alumno'
    _description = 'Alumno del Colegio'
    _rec_name = 'user_id'

    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    edad = fields.Integer("Edad", required=True)
    tutor_id = fields.Many2one('colegio.tutor', string="Tutor")
    grado = fields.Many2one('colegio.curso', string="Grado Actual")
    
    @api.model
    def create(self, vals):
        # Crear el registro de profesor
        alumno = super(Alumno, self).create(vals)
        
        # Asignar el grupo "Profesor" al usuario seleccionado
        if alumno.user_id:
            group_alumno = self.env.ref('agenda.group_alumno')
            alumno.user_id.groups_id |= group_alumno
        
        return alumno
    