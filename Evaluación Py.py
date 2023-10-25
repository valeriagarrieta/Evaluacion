class Producto:
    def _init_(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = self.calcular_precio_venta(margen_de_venta)

    def calcular_precio_venta(self, margen_de_venta):
        return self.costo / (1 - margen_de_venta)

class Inventario:
    def _init_(self):
        self.productos = {}

    def registrar_producto(self, producto):
        self.productos[producto.id] = producto

    def imprimir_listado(self):
        for producto_id, producto in self.productos.items():
            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Costo: {producto.costo}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio de Venta: {producto.precio_de_venta}")
            print()


if __name__ == "_main_":
    inventario = Inventario()

    producto1 = Producto(1, "Producto 1", "Descripción 1", 10.0, 100, 0.2)
    producto2 = Producto(2, "Producto 2", "Descripción 2", 20.0, 50, 0.3)

    inventario.registrar_producto(producto1)
    inventario.registrar_producto(producto2)

    inventario.imprimir_listado()