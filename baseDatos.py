def creacion_DB(tabla,nombre,conexion):
    
    tabla.to_sql(nombre, con = conexion, if_exists = 'replace')
    