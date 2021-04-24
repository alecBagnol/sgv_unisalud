import modulos.creacion_db as crear
import modulos.actions_db as agregar


# comentar cuando la tabla ya sea creada
crear.crear_tablas()

ciudades = [
    (None, 'Bogota'),
    (None, 'Manizales'),
    (None, 'Medellin'),
    (None, 'Palmira')
]
agregar.agregar_ciudades(ciudades)
agregar.agregar_afiliado(1018433932,"Maria Camila","Rodriguez Romero", "CL 95A 11A 25",3006998877,"macaroro@email.com",None,3082000,23042021,None,None,None)

# crear usuario
# obterner usuario por id
# desafiliar usuario 

# crear lote de vacunas
# obtener lote de vacunas por id 

# crear plan de vacunacion
# obtener plan de vacunacion por id 

# crear agenda de vacunacion
# obtener todas las agendas vacunacion
# obtener agenda de vacunacion por id
