from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Ficha, Atencion

# UTILIDAD: convertir documentos en JSON
def usuario_to_dict(u):
    return {'id': str(u.id), 'nombre': u.nombre, 'correo': u.correo, 'rol': u.rol}

def ficha_to_dict(f):
    return {'id': str(f.id), 'usuario_id': str(f.usuario.id), 'descripcion': f.descripcion, 'fecha_creacion': f.fecha_creacion}

def atencion_to_dict(a):
    return {'id': str(a.id), 'ficha_id': str(a.ficha.id), 'detalle': a.detalle, 'fecha': a.fecha}

# --- Usuarios ---
def listar_usuarios(request):
    usuarios = Usuario.objects()
    return JsonResponse([usuario_to_dict(u) for u in usuarios], safe=False)

def usuario_por_id(request, id):
    try:
        u = Usuario.objects.get(id=id)
        return JsonResponse(usuario_to_dict(u))
    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

# --- Fichas ---
def listar_fichas(request):
    fichas = Ficha.objects()
    return JsonResponse([ficha_to_dict(f) for f in fichas], safe=False)

def ficha_por_id(request, id):
    try:
        f = Ficha.objects.get(id=id)
        return JsonResponse(ficha_to_dict(f))
    except Ficha.DoesNotExist:
        return JsonResponse({'error': 'Ficha no encontrada'}, status=404)

# --- Atenciones ---
def listar_atenciones(request):
    atenciones = Atencion.objects()
    return JsonResponse([atencion_to_dict(a) for a in atenciones], safe=False)

def atencion_por_id(request, id):
    try:
        a = Atencion.objects.get(id=id)
        return JsonResponse(atencion_to_dict(a))
    except Atencion.DoesNotExist:
        return JsonResponse({'error': 'Atención no encontrada'}, status=404)
