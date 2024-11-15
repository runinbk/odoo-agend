# -*- coding: utf-8 -*-
{
    'name': 'Agenda',
    'version': '1.0',
    'depends': ['base'],
    'summary': 'Agenda Electronica Academica',
    'author': 'Diego Vargas',
    'category': 'Education',
    'description': 'Módulo de agenda escolar con alumnos, tutores, cursos, materias y profesores.',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'data/data.xml',
        'views/tutor_views.xml',
        'views/alumno_views.xml',
        'views/curso_views.xml',
        'views/gestion_views.xml',
        'views/materia_views.xml',
        'views/profesor_views.xml',
        'views/administrativo_views.xml',
        'views/notificacion_views.xml',
        'views/asignacion_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
        'data/demo_data.xml',
        'data/demo_curso.xml',
        'data/demo_materias.xml',
        'data/demo_administrativos.xml',
        'data/demo_profesores.xml',
        'data/demo_gestion.xml',
        'data/demo_tutores.xml',
        'data/demo_alumnos.xml',
        'data/demo_notificacion.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
