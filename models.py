from app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer,  primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    id_admin = db.Column(db.Boolean)

class Persona(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50)) 
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(25))
    fecha_nacimiento = db.Column(db.Date)
    direccion = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_persona = db.Column(db.String(50))
    
    id_localidad = db.Column(db.Integer, db.ForeignKey('localidades.id')) 
    id_genero = db.Column(db.Integer, db.ForeignKey('generos.id'))
    id_est_civil = db.Column(db.Integer, db.ForeignKey('estado_civil.id'))
    
    __mapper_args__ = {
        'polymorphic_on': tipo_persona,  # Columna que determina el tipo
        'polymorphic_identity': 'persona'  # Identificador para la clase base
    }

class Empleado(Persona):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, db.ForeignKey('personas.id'), primary_key=True)
    fecha_contratacion = db.Column(db.Date)
    estado = db.Column(db.Boolean, default=True)
    cuit = db.Column(db.String(25))
    
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id'))
    id_turnos = db.Column(db.Integer, db.ForeignKey('turnos.id'))
    
    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
    }
    
class Cliente(Persona):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, db.ForeignKey('personas.id'), primary_key=True)
    cuit = db.Column(db.String(25))
    fecha_alta = db.Column(db.Date)
    fecha_carga = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Boolean, default=True)

    __mapper_args__ = {
        'polymorphic_identity': 'cliente',
    }
    
class Rol(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Tipo_membresia(db.Model):
    __tablename__ = 'tipos_membresia'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    costo = db.Column(db.Integer)
    duracion_dias = db.Column(db.Integer)
    descripcion = db.Column(db.String(255))
    
    
class Membresia(db.Model):
    __tablename__ = 'membresias'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_fin = db.Column(db.DateTime) #se calcula con la duracion en tipo membresia
    estado = db.Column(db.Boolean, default=True)
    
    id_tipo_membresia = db.Column(db.Integer, db.ForeignKey('tipos_membresia.id'))
    
class Genero(db.Model):
    __tablename__ = 'generos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Estado_civil(db.Model):
    __tablename__ = 'estado_civil'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id')) #pantalones, remeras, buzos, etc
    talla = db.Column(db.String(10))
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    descripcion = db.Column(db.String(200))
    momento_carga = db.Column(db.DateTime, default=datetime.utcnow)
    
    id_marca = db.Column(db.Integer, db.ForeignKey('marcas.id'))
    
class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Maquinas(db.Model):
    __tablename__ = 'maquinas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    descripcion = db.Column(db.String(200))
    momento_carga = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Boolean, default=True) #por las dudas de que se cambie la maquina o venda
    
    id_marca = db.Column(db.Integer, db.ForeignKey('marcas.id'))
    
class Marca(db.Model):
    __tablename__ = 'marcas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Pais(db.Model):
    __tablename__ = 'paises'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Provincia(db.Model):
    __tablename__ = 'provincias'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
    id_pais = db.Column(db.Integer, db.ForeignKey('paises.id'))
    
class Localidad(db.Model):
    __tablename__ = 'localidades'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    id_provincia = db.Column(db.Integer, db.ForeignKey('provincias.id'))
    
class Sucursal(db.Model):
    __tablename__ = 'sucursales'
    
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(100))
    
class Metodo_pago(db.Model):
    __tablename__ = 'metodos_pago'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    comentario = db.Column(db.Text)
    
class Asistencia_cliente(db.Model):
    __tablename__ = 'asistencias_cliente'
    
    id = db.Column(db.Integer, primary_key=True)
    entrada = db.Column(db.DateTime, default=datetime.utcnow)
    salida = db.Column(db.DateTime)
    
class Tarjetas(db.Model):
    __tablename__ = 'tarjetas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
class Descuento(db.Model):
    __tablename__ = 'descuentos'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Float)
    
class Promocion(db.Model):
    __tablename__ = 'promociones'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    descuento = db.Column(db.Float)
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_fin = db.Column(db.DateTime)
    
    id_tipo_membresia = db.Column(db.Integer, db.ForeignKey('tipos_membresia.id'))
    
class Evaluacion_fisica(db.Model):
    __tablename__ = 'evaluaciones_fisicas'
    
    id = db.Column(db.Integer, primary_key=True)
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
    actividad_fisica_actual = db.Column(db.String(50))
    motivo_inicio = db.Column(db.Text)
    
    id_persona = db.Column(db.Integer, db.ForeignKey('personas.id'))
    
class Venta(db.Model):
    __tablename__ = 'ventas'
    
    id = db.Column(db.Integer, primary_key=True)
    id_factura = db.Column(db.Integer, db.ForeignKey('facturas.id'))
    num_venta = db.Column(db.Integer)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    id_metodo_pago = db.Column(db.Integer, db.ForeignKey('metodos_pago.id'))
    fecha_venta = db.Column(db.DateTime, default=datetime.utcnow)
    
class Detalle_venta(db.Model):
    __tablename__ = 'detalles_venta'
    
    id = db.Column(db.Integer, primary_key=True)
    id_venta = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    precio_unitario = db.Column(db.Float)
    total = db.Column(db.Float)
    id_tipo_factura = db.Column(db.Integer, db.ForeignKey('tipos_factura.id'))
    
    
class Compra(db.Model):
    __tablename__ = 'compras'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=datetime.utcnow)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('proveedores.id'))
    num_compra = db.Column(db.Integer)
    id_metodo_pago = db.Column(db.Integer, db.ForeignKey('metodos_pago.id'))
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    
class Detalle_compra(db.Model):
    __tablename__ = 'detalles_compra'
    
    id = db.Column(db.Integer, primary_key=True)
    id_compra = db.Column(db.Integer, db.ForeignKey('compras.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    precio_unitario = db.Column(db.Float)
    
class Proveedor(Persona):
    __tablename__ =  'proveedores'
    
    id = db.Column(db.Integer, db.ForeignKey('personas.id'), primary_key=True)
    cuit = db.Column(db.String(25))
    razon_social = db.Column(db.String(50))
    id_localidad = db.Column(db.Integer, db.ForeignKey('localidades.id'))
    correo = db.Column(db.String(50))
    estado = db.Column(db.Boolean, default=True)
    
    id_cond_fiscal = db.Column(db.Integer, db.ForeignKey('condicion_fiscal.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'proveedor',
    }
    
class Condicion_fiscal(db.Model):
    __tablename__ = 'condicion_fiscal'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    
    
class Factura(db.Model):
    __tablename__ = 'facturas'
    
    id = db.Column(db.Integer, primary_key=True)
    num_factura = db.Column(db.Integer)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha_emision = db.Column(db.DateTime, default=datetime.utcnow)
    id_tipo_factura = db.Column(db.Integer, db.ForeignKey('tipos_factura.id'))
    estado = db.Column(db.Boolean)
    fecha_pago = db.Column(db.DateTime)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    total = db.Column(db.Float)
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursales.id'))
    
class Detalle_factura(db.Model):
    __tablename__ = 'detalles_factura'
    
    id = db.Column(db.Integer, primary_key=True)
    id_factura = db.Column(db.Integer, db.ForeignKey('facturas.id'))
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    precio_unitario = db.Column(db.Float)
    subtotal = db.Column(db.Float)
    fecha_emision = db.Column(db.DateTime, default=datetime.utcnow)
    
class Tipo_factura(db.Model):
    __tablename__ = 'tipos_factura'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10))
    
class Turnos(db.Model):
    __tablename__ = 'turnos'
    
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))