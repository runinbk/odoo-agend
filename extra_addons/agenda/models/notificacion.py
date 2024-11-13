from odoo import models, fields, api

class Notificacion(models.Model):
    _name = 'colegio.notificacion'
    _description = 'Notificación'
    _rec_name = 'titulo'

    titulo= fields.Char(string='Título', required=True)
    mensaje = fields.Html(string='Mensaje')  # Para texto enriquecido
    fecha = fields.Date(string='Fecha')
    hora = fields.Float(
        string='Hora de Inicio',
        widget='float_time',
        help='Seleccione la hora'
    )
    tipo = fields.Char(default='comunicado')
    lugar = fields.Char(string='Lugar')
    fecha_cierre = fields.Date(string='Fecha Cierre')
    user_ids = fields.Many2many('res.users', string='Usuarios')
    attachment_ids = fields.Many2many('ir.attachment', string='Archivos Adjuntos', 
                                      help="Adjunta archivos relacionados con la notificación",
                                      relation="m2m_colegio_notificacion_attachment",
                                      domain=[('res_model', '=', 'colegio.notificacion')])
    creado_por = fields.Many2one(
        'res.users', 
        string='Creado por', 
        default=lambda self: self.env.user, 
        readonly=True
    )
    tipo_destinatario = fields.Selection([
        ('todos', 'Todos'),
        ('profesores', 'Profesores'),
        ('curso', 'Curso'),
        ('especifico', 'Específico')
    ], string="Enviar a", required=True)
    curso_id = fields.Many2one('colegio.curso', string="Curso", help="Seleccionar curso para enviar notificación", store=True)
    
    @api.model
    def create(self, vals):
        notificacion = super(Notificacion, self).create(vals)
        notificacion.crear_lecturas()
        return notificacion

    def crear_lecturas(self):
        # Lógica para generar registros en la tabla Lectura en base al tipo de destinatario seleccionado.
        users_to_notify = []

        if self.tipo_destinatario == 'todos':
            users_to_notify = self.env['res.users'].search([])

        elif self.tipo_destinatario == 'profesores':
            profesores = self.env['colegio.profesor'].search([])  # Buscamos todos los registros de colegio.profesor
            users_to_notify = profesores.mapped('user_id') # Obtenemos el user_id de cada profesor

        elif self.tipo_destinatario == 'curso' and self.curso_id:
            alumnos = self.curso_id.alumno_ids
            tutores = alumnos.mapped('tutor_id')
            users_to_notify = tutores.mapped('user_id') | alumnos.mapped('user_id')

        elif self.tipo_destinatario == 'especifico' and self.user_ids:
            users_to_notify = self.user_ids

        for user in users_to_notify:
            self.env['colegio.lectura'].create({
                'notificacion_id': self.id,
                'user_id': user.id,
            })
            
    def action_view_lecturas(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lecturas de Notificación',
            'res_model': 'colegio.lectura',
            'view_mode': 'list,form',
            'domain': [('notificacion_id', '=', self.id)],
            'context': {'default_notificacion_id': self.id},
        }

class Lectura(models.Model):
    _name = 'colegio.lectura'
    _description = 'Lectura de Notificaciones por Usuario'
    _rec_name = 'estado'

    notificacion_id = fields.Many2one('colegio.notificacion', string="Notificación", required=True)
    user_id = fields.Many2one('res.users', string="Usuario", required=True)
    estado = fields.Char("Estado", default='Enviado')
