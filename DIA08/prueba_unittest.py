import unittest

# es mas recomendado realizar las pruebas de unittest en archivos aparte al de las pruebas, usando un import
class ProbarCambiaTexto(unittest.TestCase):
    """Unittest asegura si esto se ejecuta y devuelve el resultado esperado o nop
    importante el test_ al inicio de la funcion"""
    def test_todomayus(self):
        self.assertEqual(todo_mayusculas('hola'), 'HOLA')


def todo_mayusculas(text):
    return text.upper()

if __name__ == '__main__':
    """Esto hace que el script empiece a ejecutarse por aqui si estamos en este archivo
    y no se ejecute si esta siendo importado desdde otro archivo"""
    unittest.main()
