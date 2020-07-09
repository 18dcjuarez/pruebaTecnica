
ERROR_VALUE_LESS_THAN_CERO = 'El balance no puede ser menor a 0.00'
ERROR_OBJECT_NOT_CREATED = 'No se pudo crear el objeto'
ERROR_ACCOUNT_ALREADY_EXIST = 'La cuenta ya existe'
ERROR_OWNER_ALREADY_EXIST = 'El usuario ya existe'
ERROR_ACCOUNT_DONT_EXIST = 'La cuenta no existe'
ERROR_OWNER_DONT_EXIST = 'El usuario no existe'
ERROR_TRANSACTION = 'No se pudo crear la cuenta'
ERROR_MIN_BALANCE = 'No cuentas con saldo suficiente para realizar esta transación'


class GeneralError:
    def __init__(self, message):
        self.error = {'message': message}

    def __str__(self):
        return self.error['message']
