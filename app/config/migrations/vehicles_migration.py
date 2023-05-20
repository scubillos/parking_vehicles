from ..database import conn

def migrate():
    create_database_query = """
    CREATE DATABASE IF NOT EXISTS parking_vehicles;
    """

    drop_table_query = """
    DROP TABLE IF EXISTS vehicles;
    """

    create_table_query = """
    CREATE TABLE vehicles (
        id INT AUTO_INCREMENT PRIMARY KEY,
        plat_number VARCHAR(10),
        name VARCHAR(100),
        registration_number VARCHAR(100),
        status INT DEFAULT 0,
        type VARCHAR(10),
        packing_charge INT DEFAULT 0
    );
    """

    cursor = conn.cursor()

    # Crear la base de datos si no existe
    #cursor.execute(create_database_query)
    #conn.commit()

    # Seleccionar la base de datos
    cursor.execute("USE parking_vehicles")

    # Ejecutar DROP TABLE solo si existe
    # cursor.execute(drop_table_query)

    # Recuperar completamente los resultados antes de continuar
    while cursor.nextset():
        pass

    cursor.execute(create_table_query)

    # Recuperar completamente los resultados antes de continuar
    while cursor.nextset():
        pass

    conn.commit()

    cursor.close()
    conn.close()