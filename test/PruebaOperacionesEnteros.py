import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros

class PruebaOperacionesEnteros(unittest.TestCase):
    
    def setUp(self):
        self.operacion = OperacionesEnteros([])

    def tearDown(self):
        self.operacion = None

    def test_MCD_dosNumerosPositivos_retornaMCD(self):
        
        # Arrange
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 6
        operacion = OperacionesEnteros([numero1, numero2])

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_tresNumerosPositivos_retornaMCD(self):
        
        # Arrange
        numero1 = 24679
        numero2 = 20387
        numero3 = 16169
        resultadoEsperado = 37
        
        operacion = OperacionesEnteros([numero1, numero2, numero3])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)
        
    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        
        # Arrange  
        numero1 = 18
        numero2 = 9
        numero3 = 27
        numero4 = 54
        resultadoEsperado = 9
        
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])
        
        # Do
        resultadoActual = operacion.calcularMCD()
        
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cincoNumerosPositivos_retornaMCD(self):
        
        # Arrange
        numero1 = 36
        numero2 = 28
        numero3 = 54
        numero4 = 46
        numero5 = 60
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4, numero5])
        
        # Do
        resultadoActual = operacion.calcularMCD()
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_unNumeroPositivo_lanzaExcepcion(self):
        numero1 = 54
        operacion = OperacionesEnteros([numero1])

        self.assertTrue(True)
        with self.assertRaises(FaltanParametros):
            operacion.calcularMCD()
                  
    def test_MCD_unaCadena_lanzaExcepcion(self):
        numero1 = "h"
        numero2 = 26
        operacion = OperacionesEnteros([numero1, numero2])

        self.assertTrue(True)
        with self.assertRaises(ValueError):
            operacion.calcularMCD()
        
