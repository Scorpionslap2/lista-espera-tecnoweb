from mongoengine import Document, StringField, EmailField, ReferenceField, DateTimeField
from datetime import datetime

class Usuario(Document):
    nombre = StringField(required=True, max_length=100)
    correo = EmailField(required=True, unique=True)
    contraseña = StringField(required=True, min_length=6)
    rol = StringField(required=True, choices=["admin", "medico", "paciente"])

class Ficha(Document):
    usuario = ReferenceField(Usuario, required=True)
    descripcion = StringField()
    fecha_creacion = DateTimeField(default=datetime.utcnow)

class Atencion(Document):
    ficha = ReferenceField(Ficha, required=True)
    detalle = StringField()
    fecha = DateTimeField(default=datetime.utcnow)
