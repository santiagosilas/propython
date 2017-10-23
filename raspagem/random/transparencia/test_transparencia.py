# coding: utf-8
import transparencia as t
import unittest

class TestTransparenciaFunctions(unittest.TestCase):
    def test_obter_remuneracao_servidor(self):
        pagina = t.obter_pagina_servidores(1)
        sopa, success = t.validar_pagina_servidores(pagina)
        self.assertEqual(pagina.status_code, 200)
        self.assertEqual(success, True)
        lista = t.listar_servidores_pagina(sopa)
        self.assertEqual(type(lista), list)
        self.assertNotEqual(len(lista), 0)
        servidor = lista[0]
        valor = t.obter_remuneracao_servidor(servidor[1])
        self.assertEqual(valor, '6333.60')
        
        
if __name__ == '__main__':
    unittest.main()
