-- =====================================================================
-- SCRIPT DE INSERCIÓN DE DATOS (SEED DATA) PARA BIBLIOTECA UNIVERSITARIA
-- =====================================================================

TRUNCATE TABLE gestion_editorial, gestion_estudiante, gestion_credencial, gestion_libro, gestion_prestamo RESTART IDENTITY CASCADE;



-- 1. Insertar 10 Editoriales
INSERT INTO gestion_editorial (nombre) VALUES
('Editorial Universitaria'),
('McGraw Hill Education'),
('Pearson Educación'),
('OReilly Media'),
('Addison-Wesley'),
('Prentice Hall'),
('Ediciones Paraninfo'),
('Marcombo'),
('Cengage Learning'),
('Siglo XXI Editores');

-- 2. Insertar 10 Estudiantes
INSERT INTO gestion_estudiante (matricula, nombre_completo) VALUES
('MAT-2023-001', 'Ana Sofía Martínez'),
('MAT-2023-002', 'Carlos Eduardo López'),
('MAT-2023-003', 'María Fernanda Gómez'),
('MAT-2023-004', 'Juan Pablo Ramírez'),
('MAT-2023-005', 'Laura Valentina Torres'),
('MAT-2023-006', 'Diego Alejandro Ruiz'),
('MAT-2023-007', 'Camila Andrea Díaz'),
('MAT-2023-008', 'Javier Ignacio Morales'),
('MAT-2023-009', 'Valentina Castro'),
('MAT-2023-010', 'Santiago Herrera');

-- 3. Insertar 10 Credenciales (Relación 1 a 1 con Estudiante)
-- Suponemos que los IDs de los estudiantes generados arriba son 1 a 10.
INSERT INTO gestion_credencial (estudiante_id, codigo_barras, fecha_expedicion, activa) VALUES
(1, 'CRED-MAT-2023-001', CURRENT_DATE, TRUE),
(2, 'CRED-MAT-2023-002', CURRENT_DATE, TRUE),
(3, 'CRED-MAT-2023-003', CURRENT_DATE, TRUE),
(4, 'CRED-MAT-2023-004', CURRENT_DATE, TRUE),
(5, 'CRED-MAT-2023-005', CURRENT_DATE, TRUE),
(6, 'CRED-MAT-2023-006', CURRENT_DATE, TRUE),
(7, 'CRED-MAT-2023-007', CURRENT_DATE, TRUE),
(8, 'CRED-MAT-2023-008', CURRENT_DATE, TRUE),
(9, 'CRED-MAT-2023-009', CURRENT_DATE, TRUE),
(10, 'CRED-MAT-2023-010', CURRENT_DATE, TRUE);

-- 4. Insertar 10 Libros (Relación 1 a N con Editorial)
INSERT INTO gestion_libro (titulo, editorial_id, stock_disponible) VALUES
('Introducción a la Algoritmia', 1, 5),
('Cálculo Estructural Avanzado', 2, 3),
('Sistemas Operativos Modernos', 3, 4),
('Clean Code: Programación Ágil', 4, 10),
('Diseño de Patrones de Software', 5, 2),
('Física Universitaria Vol. 1', 3, 8),
('Química Orgánica Básica', 2, 5),
('Bases de Datos Relacionales', 6, 7),
('Inteligencia Artificial: Un Enfoque Moderno', 3, 4),
('Arquitectura de Computadoras', 8, 6);

-- 5. Insertar 10 Préstamos (Relación N a M manual: Estudiantes y Libros)
INSERT INTO gestion_prestamo (estudiante_id, libro_id, fecha_prestamo, fecha_devolucion, estado, multa_generada) VALUES
(1, 1, CURRENT_TIMESTAMP - INTERVAL '10 days', NULL, 'Activo', 0.0),
(2, 4, CURRENT_TIMESTAMP - INTERVAL '5 days', NULL, 'Activo', 0.0),
(3, 8, CURRENT_TIMESTAMP - INTERVAL '15 days', CURRENT_TIMESTAMP - INTERVAL '2 days', 'Devuelto', 0.0),
(4, 9, CURRENT_TIMESTAMP - INTERVAL '30 days', NULL, 'Activo', 0.0), -- Candidato a multa alta
(5, 2, CURRENT_TIMESTAMP - INTERVAL '2 days', NULL, 'Activo', 0.0),
(6, 3, CURRENT_TIMESTAMP - INTERVAL '12 days', NULL, 'Activo', 0.0),
(7, 4, CURRENT_TIMESTAMP - INTERVAL '20 days', CURRENT_TIMESTAMP - INTERVAL '1 day', 'Devuelto', 5.50), -- Ya tuvo multa y fue devuelto
(8, 5, CURRENT_TIMESTAMP - INTERVAL '8 days', NULL, 'Activo', 0.0),
(9, 7, CURRENT_TIMESTAMP - INTERVAL '3 days', NULL, 'Activo', 0.0),
(10, 10, CURRENT_TIMESTAMP - INTERVAL '45 days', NULL, 'Activo', 0.0); -- Candidato a multa máxima
