from odoo import models, fields, api

class Tutor(models.Model):
    _name = 'colegio.tutor'
    _description = 'Tutor o Apoderado'
    _rec_name = '_tutor_rec'
    
    parentesco = fields.Char("Parentesco Familiar", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    alumno_ids = fields.One2many('colegio.alumno', 'tutor_id', string="Alumnos")
    
    # Campo computado para concatenar nombre y nivel
    _tutor_rec = fields.Char(compute='_compute_name', store=False)
    
    @api.model
    def create(self, vals):
        # Crear el registro de profesor
        tutor = super(Tutor, self).create(vals)
        
        # Asignar el grupo "Profesor" al usuario seleccionado
        if tutor.user_id:
            group_tutor = self.env.ref('agenda.group_tutor')
            tutor.user_id.groups_id |= group_tutor
        
        return tutor
    
    @api.depends('user_id', 'parentesco')
    def _compute_name(self):
        for record in self:
            record._tutor_rec = f"{record.user_id.display_name} - {record.parentesco}"