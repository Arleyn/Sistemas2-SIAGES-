# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE SOLICITUD                               #
#------------------------------------------------------------------------------#

db.define_table('Solicitud',
    Field('prioridad',
          type='string',
          label=T('Prioridad'),
          default='Normal'),
    Field('fecha_realizacion',
          type='date',
          label=T('Fecha de Solicitud'),
          default=request.now,
          writable=False),
    Field('area',
          db.Area,
          requires = IS_IN_DB(db, db.Area.id,'%(nombre_area)s'),
          label=T('(*) Area de Trabajo')),
    Field('tipo',
          label=T('(*) Tipo'),
          requires = IS_IN_SET(['Departamento de Mantenimiento', 'Departamento de Planificación', 'Departamento de Proyectos'])),
    Field('unidad',
          db.Unidad,
          requires = IS_IN_DB(db, db.Unidad.id,'%(nombre_unidad)s'),
          label=T('(*) Unidad Solicitante')),
    Field('nombre_contacto',
          label=T('(*) Persona Contacto'),
          requires=IS_NOT_EMPTY()),
    Field('info_contacto',
          label=T('(*) Email de Contacto'),
          requires= [IS_EMAIL(error_message='Debe introducir el correo electronico del solicitante.'),
                     IS_NOT_EMPTY()]),
    Field('edificio',
          db.Edificio,
          requires = IS_IN_DB(db, db.Edificio.id, '%(nombre_edificio)s'),
          label=T('(*) Edificio')),
    Field('espacio',
          db.Lugar,
          requires = IS_IN_DB(db, db.Lugar.id,'%(espacio)s'),
          label=T('(*) Espacio')),
    Field('telefono',
          label=T('Telefono (Extensión)'),
          type='integer'),
    Field('requerimiento',
          type='text',
          label=T('(*) Requerimiento'),
          requires=IS_NOT_EMPTY()),
    Field('observacion_solicitud',
          type='text',
          label=T('Observaciones')),
    Field('supervisor',
          type='string',
          label=T('Supervisor Responsable'),
          default=''),
    Field('fecha_inicio',
          type='date',
          label=T('Fecha de inicio')),
    Field('fecha_culminacion',
          type='date',
          label=T('Fecha de culminación')),
    Field('trabajador',
         type='list:string',
         label=T('Trabajadores Asignados'),
         default=['1.', '2.', '3.', '4.', '5.', '6.']),
    Field('observacion_ejecucion',
          type='text',
          label=T('Observaciones de Ejecución')),
    Field('status',
          #requires = IS_IN_DB(db, db.Status_solicitud.nombre_status,'%(nombre_status)s'),
          label=T('Estado')),
          default ='Urgente'
    )
db.Solicitud.id.label=T('Numero de Solicitud')

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
