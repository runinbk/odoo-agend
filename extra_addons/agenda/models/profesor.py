from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'colegio.profesor'
    _description = 'Profesor del Colegio'
    _rec_name = 'user_id'

    especialidad = fields.Char("Especialidad", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    asignacion_ids = fields.One2many('colegio.asignacion', 'profesor_id', string="Asignaciones")
    
    @api.model
    def create(self, vals):
        # Crear el registro de profesor
        profesor = super(Profesor, self).create(vals)
        
        # Asignar el grupo "Profesor" al usuario seleccionado
        if profesor.user_id:
            group_profesor = self.env.ref('agenda.group_profesor')
            profesor.user_id.groups_id |= group_profesor
        
        return profesor
