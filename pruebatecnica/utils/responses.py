from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.http import Http404


def create_response(success: bool, status: int, data: object, message: object, code: int):

    status = 200
    if success:
        code = 200

    else:
        if hasattr(message, 'error'):
            err = message.error
            message = err.message
            code = err.code

        # El nombre no está asociado a ninguna variable.
        elif isinstance(message, UnboundLocalError):
            message = str(message)
            code = 401

        #
        elif isinstance(message, FieldError):
            message = str(message)
            code = 402

        elif isinstance(message, Http404):
            message = str(message)
            code = 403

        elif isinstance(message, ObjectDoesNotExist):
            message = str(message)
            code = 404
        #
        elif isinstance(message, OverflowError):
            message = str(message)
            code = 405

        # Valor del argumento no apropiado
        elif isinstance(message, ValueError):
            message = str(message)
            code = 406

        # Tipo de argumento no apropiado
        elif isinstance(message, TypeError):
            message = str(message)
            code = 407

        # Error interno del intérprete
        elif isinstance(message, SystemError):
            message = str(message)
            code = 408

        # Ese método o función no está implementado.
        elif isinstance(message, NotImplementedError):
            message = str(message)
            code = 409

        # Error en tiempo de ejecución no especificado.
        elif isinstance(message, RuntimeError):
            message = str(message)
            code = 410

        # No se encontró ningún elemento con ese nombre.
        elif isinstance(message, NameError):
            message = str(message)
            code = 411

        # No queda memoria suficiente
        elif isinstance(message, MemoryError):
            message = str(message)
            code = 412

        # La clave no existe
        elif isinstance(message, KeyError):
            message = str(message)
            code = 413

        # El índice de la secuencia está fuera del rango posible
        elif isinstance(message, IndexError):
            message = str(message)
            code = 414

        # No se encuentra el módulo o el elemento del módulo que se quería importar
        elif isinstance(message, ImportError):
            message = str(message)
            code = 415

        # Error en una llamada a sistema
        elif isinstance(message, OSError):
            message = str(message)
            code = 416

        # No se encontró el atributo
        elif isinstance(message, AttributeError):
            message = str(message)
            code = 417

        # Clase padre para los errores sintácticos
        elif isinstance(message, SyntaxError):
            message = str(message)
            code = 418

        elif isinstance(message, BaseException):
            message = str(message)
            code = 500
            status = 500

    response = {
        'success': success,
        'code': code,
        'data': data,
        'message': message
    }

    return Response(response, status=status)
