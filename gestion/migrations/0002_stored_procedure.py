from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
            CREATE OR REPLACE PRODUCEDURE sp_calcular_multa(p_estudiante_id INT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                UPDATE gestion_prestamo
                SET multa_generado = 25.50
                WHERE estudiante_id = p_estudiante_id
                  AND estado = 'Activo';
                COMMIT;
            END;
            $$;
           ''',
            reverse_sql=
            '''
            DROP PROCEDURE IF EXISTS sp_calcular_multa;
           '''
        ),
    ]
