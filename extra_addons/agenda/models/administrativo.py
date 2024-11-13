from odoo import models, fields, api

class Administrativo(models.Model):
    _name = 'colegio.administrativo'
    _description = 'Personal Administrativo del Colegio'
    _rec_name = 'user_id'

    cargo = fields.Char("Cargo", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    
    @api.model
    def create(self, vals):
        # Crear el registro de administrativo
        administrativo = super(Administrativo, self).create(vals)
        
        # Asignar el grupo "Profesor" al usuario seleccionado
        if administrativo.user_id:
            group_administrativo = self.env.ref('agenda.group_administrativo')  # Cambia 'tu_modulo' por el nombre real de tu módulo
            administrativo.user_id.groups_id |= group_administrativo
        
        return administrativo
