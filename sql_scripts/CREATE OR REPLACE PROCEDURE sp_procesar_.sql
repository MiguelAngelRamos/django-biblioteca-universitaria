CREATE OR REPLACE PROCEDURE sp_procesar_nuevo_pedido(
  p_cliente_id INT, 
  p_producto_id INT, 
  p_cantidad INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_precio_unitario NUMERIC(10, 2);
    v_stock_actual INT;
    v_pedido_id INT;
BEGIN
    -- INTO se utiliza para capturar el resultado de una consulta SQL y guardarlo directamente dentro de las variables locales que creaste en tu bloque DECLARE.
    SELECT precio, stock INTO v_precio_unitario, v_stock_actual FROM productos WHERE producto_id = p_producto_id;

    IF v_precio_unitario IS NULL THEN
        RAISE EXCEPTION 'Error: Producto % no existe o no tiene asignado un precio', p_producto_id;
    END IF;

    IF v_stock_actual < p_cantidad THEN
        RAISE EXCEPTION 'Error: Stock insuficiente para el producto %', p_producto_id;
    END IF;

    -- Insertar el nuevo pedido
    INSERT INTO pedidos(cliente_id, fecha_pedido, estado) 
    VALUES (p_cliente_id, CURRENT_TIMESTAMP, 'Enviado') 
    RETURNING pedido_id INTO v_pedido_id;

    -- Insertar los detalles del pedido
    INSERT INTO detalles_pedido(pedido_id, producto_id, cantidad, precio_unitario)
    VALUES (v_pedido_id, p_producto_id, p_cantidad, v_precio_unitario);

    -- Descontar del stock del producto
    UPDATE productos
    SET stock = stock - p_cantidad
    WHERE producto_id = p_producto_id;

    COMMIT;
    RAISE NOTICE 'Pedido #% creado exitosamente para el cliente #%', v_pedido_id, p_cliente_id;
    -- El pedido #10 creado exitosamente para el cliente #50

END;
$$;